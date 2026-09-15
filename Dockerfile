FROM python:3.12-slim AS docs

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]

# Estágio usado apenas pelos checks de qualidade: adiciona o linkchecker
# por cima da imagem da documentação.
FROM docs AS quality

RUN pip install --no-cache-dir -r requirements-dev.txt

CMD ["./scripts/check-links.sh"]

# Estágio isolado do dashboard de QA: dependências próprias (qa-analytics/requirements.txt),
# sem misturar com o ambiente do MkDocs.
FROM python:3.12-slim AS qa-analytics

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY qa-analytics/requirements.txt qa-analytics/requirements.txt

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r qa-analytics/requirements.txt

COPY qa-analytics/ qa-analytics/

WORKDIR /app/qa-analytics

EXPOSE 8501

CMD ["streamlit", "run", "dashboard.py", "--server.address=0.0.0.0", "--server.port=8501"]

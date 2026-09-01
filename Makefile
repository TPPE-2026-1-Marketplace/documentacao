COMPOSE := docker compose

# Roda os containers com o usuário do host para que os arquivos gerados
# (site estático, correções do markdownlint) não fiquem pertencendo ao root.
HOST_USER := $(shell id -u):$(shell id -g)

.PHONY: help serve build stop lint-md lint-md-fix check-links check-links-extern quality slides slides-pdf clean

help:
	@echo "Targets disponíveis (todos rodam via Docker):"
	@echo "  make serve               sobe a documentação em http://localhost:8000"
	@echo "  make build               gera o site estático em ./site"
	@echo "  make stop                para o container da documentação"
	@echo "  make lint-md             valida o estilo do Markdown (markdownlint-cli2)"
	@echo "  make lint-md-fix         corrige automaticamente o que for corrigível"
	@echo "  make check-links         build --strict + checagem de links internos"
	@echo "  make check-links-extern  idem, incluindo links externos (usa rede)"
	@echo "  make quality             roda lint-md + check-links"
	@echo "  make slides              gera as apresentações em HTML (slides/dist/)"
	@echo "  make slides-pdf          gera as apresentações em HTML e PDF"
	@echo "  make clean               remove containers e imagens locais"

serve:
	$(COMPOSE) up --build docs

build:
	$(COMPOSE) run --rm --no-deps --user $(HOST_USER) docs mkdocs build --strict

stop:
	$(COMPOSE) down

lint-md:
	$(COMPOSE) run --rm lint-md

lint-md-fix:
	$(COMPOSE) run --rm --user $(HOST_USER) lint-md --fix

check-links:
	$(COMPOSE) run --rm check-links

check-links-extern:
	$(COMPOSE) run --rm check-links ./scripts/check-links.sh --extern

quality: lint-md check-links

slides:
	./scripts/build-slides.sh

slides-pdf:
	./scripts/build-slides.sh --pdf

clean:
	$(COMPOSE) down --rmi local --remove-orphans

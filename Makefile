PYTHON := python3
VENV := .venv
PIP := $(VENV)/bin/pip
MKDOCS := $(VENV)/bin/mkdocs
STAMP := $(VENV)/.installed

.PHONY: help install serve build clean rebuild

help:
	@echo "Targets disponíveis:"
	@echo "  make install  -> instala dependências (somente se necessário)"
	@echo "  make serve    -> roda mkdocs serve (rápido)"
	@echo "  make build    -> gera site estático"
	@echo "  make clean    -> remove .venv"
	@echo "  make rebuild  -> recria tudo do zero"

# Cria o ambiente virtual apenas se não existir
$(VENV):
	$(PYTHON) -m venv $(VENV)

# Instala dependências apenas se requirements.txt mudou
$(STAMP): requirements.txt | $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	touch $(STAMP)

install: $(STAMP)

serve:
	$(MKDOCS) serve

build:
	$(MKDOCS) build

clean:
	rm -rf $(VENV)

rebuild: clean install

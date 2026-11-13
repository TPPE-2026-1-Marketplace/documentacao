# Makefile da documentação. Todos os comandos rodam via Docker (compose.yaml).
# `make help` é gerado a partir dos comentários `## ` de cada alvo e dos
# títulos `##@`, no mesmo formato do backend e do frontend. Cada alvo declara
# o próprio `.PHONY` logo acima dele.

COMPOSE := docker compose

# Roda os containers com o usuário do host para que os arquivos gerados
# (site estático, correções do markdownlint) não fiquem pertencendo ao root.
HOST_USER := $(shell id -u):$(shell id -g)

.DEFAULT_GOAL := help

##@ Setup

.PHONY: help
help: ## Lista os comandos disponíveis
	@awk 'BEGIN { FS = ":.*## " } \
		/^##@/ { printf "\n%s\n", substr($$0, 5) } \
		/^[a-zA-Z0-9_-]+:.*## / { printf "  make %-22s %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
	@echo ""

# Aponta o Git para os hooks versionados: o commit-msg preenche os
# Co-authored-by do trio. Basta rodar uma vez por clone.
.PHONY: hooks
hooks: ## Ativa o commit-msg versionado (.githooks)
	git config core.hooksPath .githooks
	@echo "Hooks ativados a partir de .githooks/"

.PHONY: hooks-off
hooks-off: ## Desativa o commit-msg versionado (volta para .git/hooks)
	git config --unset core.hooksPath || true
	@echo "Hooks desativados (voltando para .git/hooks)"

##@ Documentação

.PHONY: serve
serve: ## Sobe a documentação em http://localhost:8000
	$(COMPOSE) up --build docs

.PHONY: serve-background
serve-background: ## Sobe a documentação em background (libera o terminal)
	$(COMPOSE) up --build --detach docs

.PHONY: build
build: ## Gera o site estático em ./site
	$(COMPOSE) run --rm --no-deps --user $(HOST_USER) docs mkdocs build --strict

.PHONY: stop
stop: ## Para o container da documentação
	$(COMPOSE) down

##@ Qualidade

.PHONY: lint-md
lint-md: ## Valida o estilo do Markdown (markdownlint-cli2)
	$(COMPOSE) run --rm lint-md

.PHONY: lint-md-fix
lint-md-fix: ## Corrige automaticamente o que for corrigível no Markdown
	$(COMPOSE) run --rm --user $(HOST_USER) lint-md --fix

.PHONY: check-links
check-links: ## Build --strict + checagem de links internos
	$(COMPOSE) run --rm check-links

.PHONY: check-links-extern
check-links-extern: ## Idem, incluindo links externos (usa rede)
	$(COMPOSE) run --rm check-links ./scripts/check-links.sh --extern

.PHONY: quality
quality: lint-md check-links ## Roda lint-md + check-links

##@ Apresentações

.PHONY: slides
slides: ## Gera as apresentações em HTML (slides/dist/)
	./scripts/build-slides.sh

.PHONY: slides-pdf
slides-pdf: ## Gera as apresentações em HTML e PDF
	./scripts/build-slides.sh --pdf

##@ Dashboard de QA

.PHONY: qa-serve
qa-serve: ## Sobe o dashboard de QA em http://localhost:8501
	$(COMPOSE) up --build qa-analytics

.PHONY: qa-stop
qa-stop: ## Para o container do dashboard de QA
	$(COMPOSE) stop qa-analytics

##@ Utilidades

.PHONY: clean
clean: ## Remove containers e imagens locais
	$(COMPOSE) down --rmi local --remove-orphans

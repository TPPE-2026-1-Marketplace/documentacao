# AGENTS.md

## Repository Layout

- `docs/`: conteúdo da documentação em Markdown.
- `docs/assets/`: arquivos estáticos usados pela documentação.
- `mkdocs.yml`: configuração principal do MkDocs e navegação do site.
- `requirements.txt`: dependências Python do projeto.
- `requirements-dev.txt`: dependências das ferramentas de qualidade (LinkChecker).
- `Makefile`: atalhos para os fluxos com Docker.
- `Dockerfile`: imagem base para executar o MkDocs em container (estágios `docs` e `quality`).
- `compose.yaml`: orquestração local do container da documentação e dos checks.
- `scripts/check-links.sh`: build estrito + varredura de links quebrados.
- `scripts/build-slides.sh`: gera as apresentações de sprint com o Marp.
- `slides/`: fontes das apresentações (`template.md` é o modelo); a saída vai
  para `slides/dist/`, que não é versionada.
- `docs/sprints.md`: mapa das sprints; `docs/sprints/template.md` é o modelo de
  relatório, organizado por clans (Infra/DE, Design/K, Front/G).
- `.markdownlint-cli2.jsonc`: regras de lint do Markdown.
- `.linkcheckerrc`: configuração do LinkChecker.
- `.github/workflows/quality.yml`: CI de qualidade (lint + links).
- `README.md`: instruções para pessoas do time.

## How To Run The Project

O fluxo oficial é Docker. Não há mais suporte a `.venv` no `Makefile`; rodar o
MkDocs direto na máquina continua possível, mas não é o caminho documentado.

1. Subir a documentação:
   - `make serve`
2. Acessar:
   - `http://localhost:8000`
3. Parar o container:
   - `make stop`

## Build, Test, And Lint Commands

### Build

- Gerar site estático em `./site`:
  - `make build`

### Validation

- Validar a configuração do Compose:
  - `docker compose config`
- Verificar se a documentação compila:
  - `make build`

### Lint / tests

- Estilo do Markdown (`markdownlint-cli2`):
  - `make lint-md`
  - `make lint-md-fix` corrige o que for corrigível automaticamente
- Links quebrados (`mkdocs build --strict` + LinkChecker):
  - `make check-links`
  - `make check-links-extern` inclui links externos (depende de rede)
- Ambos de uma vez:
  - `make quality`
- Apresentações de sprint (Marp):
  - `make slides` / `make slides-pdf`
- Os dois checks rodam no CI a cada Pull Request pelo workflow `docs quality`.
  A checagem de links externos é informativa e não bloqueia o merge.
- Não há suíte de testes automatizados neste repositório.

## Engineering Conventions

- Preserve a estrutura atual do MkDocs e atualize `mkdocs.yml` quando adicionar, remover ou renomear páginas.
- Prefira mudanças pequenas e focadas.
- Ao alterar instruções de execução, mantenha `README.md` e `docs/index.md` sincronizados.
- Ao adicionar novos artefatos de infraestrutura, documente o fluxo de uso.
- Use ASCII por padrão em arquivos novos ou editados, salvo necessidade clara.
- Não introduza dependências novas sem necessidade objetiva.

## PR Expectations

- Explique claramente o que mudou, por que mudou e como validar.
- Destaque impacto em execução local, Docker, navegação do MkDocs ou estrutura de arquivos.
- Se houver mudança visível na documentação, cite as páginas afetadas.
- Inclua os comandos usados para validar a alteração.

## Constraints And Do-Not Rules

- Não reintroduzir targets baseados em `.venv` no `Makefile`: o fluxo suportado é Docker.
- Não editar conteúdo de documentação sem manter consistência com a navegação em `mkdocs.yml`.
- Não versionar artefatos gerados, como `site/`.
- Não desabilitar regras do markdownlint apenas para "passar" no CI: corrija o
  conteúdo, ou justifique a exceção com comentário em `.markdownlint-cli2.jsonc`.
- Não adicionar ferramentas pesadas de build/deploy sem necessidade explícita.

## What Done Means

Uma tarefa está concluída quando:

- a mudança necessária foi implementada;
- o fluxo principal afetado está documentado;
- `make build` executa com sucesso;
- `make quality` passa sem erros;
- se a tarefa envolver Docker, `docker compose config` permanece válido e o fluxo `make serve` continua funcional;
- não há inconsistência entre `README.md`, `docs/index.md`, `Makefile` e arquivos de infraestrutura relevantes.

## Verification Checklist

- `make quality`
- `make build`
- `docker compose config`
- se a mudança envolver container: `make serve`
- revisar páginas afetadas no navegador em `http://localhost:8000`

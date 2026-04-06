# AGENTS.md

## Repository Layout

- `docs/`: conteúdo da documentação em Markdown.
- `docs/assets/`: arquivos estáticos usados pela documentação.
- `mkdocs.yml`: configuração principal do MkDocs e navegação do site.
- `requirements.txt`: dependências Python do projeto.
- `Makefile`: atalhos para fluxos locais e com Docker.
- `Dockerfile`: imagem base para executar o MkDocs em container.
- `compose.yaml`: orquestração local do container da documentação.
- `README.md`: instruções para pessoas do time.

## How To Run The Project

### Local Python flow

1. Criar ou reutilizar o ambiente virtual:
   - `make install`
2. Rodar a documentação:
   - `make serve`
   - ou `.venv/bin/mkdocs serve`
3. Acessar:
   - `http://127.0.0.1:8000`

### Docker flow

1. Construir e subir o container:
   - `docker compose up --build`
   - ou `make docker-serve`
2. Acessar:
   - `http://localhost:8000`
3. Parar o container:
   - `docker compose down`
   - ou `make docker-stop`

## Build, Test, And Lint Commands

### Build

- Gerar site estático localmente:
  - `make build`
- Construir a imagem Docker:
  - `make docker-build`

### Validation

- Validar a configuração do Compose:
  - `docker compose config`
- Verificar se a documentação compila:
  - `make build`

### Lint / tests

- Este repositório não possui etapa formal de lint nem suíte de testes automatizados no momento.
- A validação mínima esperada é garantir que o MkDocs sobe sem erro e que o build estático funciona.

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

- Não remover ou quebrar o fluxo atual com `.venv` ao adicionar melhorias no fluxo Docker.
- Não editar conteúdo de documentação sem manter consistência com a navegação em `mkdocs.yml`.
- Não versionar artefatos gerados, como `site/`.
- Não assumir a existência de lint, CI ou testes automatizados que não estejam configurados no repositório.
- Não adicionar ferramentas pesadas de build/deploy sem necessidade explícita.

## What Done Means

Uma tarefa está concluída quando:

- a mudança necessária foi implementada;
- o fluxo principal afetado está documentado;
- `make build` executa com sucesso;
- se a tarefa envolver Docker, `docker compose config` permanece válido e o fluxo `docker compose up --build` continua funcional;
- não há inconsistência entre `README.md`, `docs/index.md`, `Makefile` e arquivos de infraestrutura relevantes.

## Verification Checklist

- `make build`
- `docker compose config`
- se a mudança envolver container: `docker compose up --build`
- revisar páginas afetadas no navegador em `http://localhost:8000` ou `http://127.0.0.1:8000`

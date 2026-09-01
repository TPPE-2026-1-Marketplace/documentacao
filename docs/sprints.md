# Sprints

Esta página é o mapa da organização das sprints do projeto: onde fica cada
relatório, como a equipe está dividida e qual é o fluxo para registrar uma nova
sprint e gerar a apresentação correspondente.

## Organização em clans

As entregas são organizadas em três clans. Cada relatório de sprint traz uma
tabela de contribuições por clan, além das entregas coletivas da equipe.

| Clan | Sigla | Escopo | Integrantes |
| --- | --- | --- | --- |
| Clan Infra | DE | \[definir escopo] | \[definir integrantes] |
| Clan Design | K | \[definir escopo] | \[definir integrantes] |
| Clan Front | G | \[definir escopo] | \[definir integrantes] |

## Índice das sprints

| Sprint | Período | Status | Relatório | Slides |
| --- | --- | --- | --- | --- |
| Sprint 01 | \[data início – data fim] | Em andamento | [Relatório](sprints/01.md) | `slides/dist/01.html` |

<!--
Ao fechar uma sprint, adicione a linha correspondente acima e atualize o
status. Status sugeridos: Planejada, Em andamento, Concluída.
-->

## Modelo de relatório

Todo relatório parte de [`docs/sprints/template.md`](sprints/template.md), que
já contém as sete seções esperadas:

1. Objetivos da Sprint
2. Entregas Coletivas
3. Contribuições dos Clans — uma tabela por clan
4. Maiores Avanços
5. Maiores Dificuldades
6. Lições Aprendidas
7. Planejamento para a Próxima Sprint

Nas seções 4, 5 e 6, quando a observação for específica de um clan, use o
formato **"Clan Infra (DE) observou que ..."**. Itens que valem para a equipe
toda ficam sem atribuição.

## Como registrar uma nova sprint

1. Copie o modelo para o número da sprint:

```bash
cp docs/sprints/template.md docs/sprints/02.md
```

1. Preencha o relatório e adicione a página ao `nav` do `mkdocs.yml`.
1. Acrescente a linha da sprint no índice desta página.
1. Rode os checks antes de abrir o Pull Request:

```bash
make quality
```

## Como gerar a apresentação

Os slides são gerados com [Marp](https://marp.app/) a partir dos arquivos em
`slides/`, usando o modelo `slides/template.md`:

```bash
cp slides/template.md slides/02.md   # edite o conteúdo da sprint
make slides                          # gera HTML em slides/dist/
make slides-pdf                      # gera também o PDF
```

A geração roda em container, sem instalar o Marp na máquina. Os arquivos de
saída ficam em `slides/dist/` e não são versionados.

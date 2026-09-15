# DK Fashion - Sprint 1 - Documento de Entrega

Documento final de entrega da Sprint 1 do projeto DK Fashion (disciplina
GCES). Consolida atividades esperadas x realizadas dos 3 trios, com
evidência real extraída do histórico de commits e Pull Requests de
`MarketPlace-Backend` e `MarketPlace-Frontend` (org TPPE-2026-1-Marketplace),
cruzado com o conteúdo do slide `GCES - Sprint 1 .pdf`.

## Visão geral da sprint

| | |
|---|---|
| Squad | 9 integrantes, em 3 trios |
| Período | 05/09/2026 a 15/09/2026 |
| Repositórios | `MarketPlace-Backend`, `MarketPlace-Frontend` |
| Reuniões (Teams) | 05/09 (início), 09/09 (alinhamento entre grupos), 14/09 (alinhamento da apresentação) |

## Equipe

| Trio | Integrantes |
|---|---|
| Grupo 1 | Bruno Bragança, Eduardo Sandes, Marcio Costa |
| Grupo 2 | Ana Luiza Aroeira, Gabriel Anjos, Leonardo Sauma |
| Grupo 3 | Ana Luiza Carvalho, Yzabella Miranda, Mateus Consorte |

## Resumo por trio

**Grupo 1**, qualidade e observabilidade: integrou SonarCloud no Backend e
no Frontend, montou o pipeline de coleta e exportação de métricas de
qualidade (`parser.py` + workflow de CI) e produziu o dashboard de
acompanhamento, além de trabalho de documentação em repositório à parte.

**Grupo 2**, hardening de produção e novas features: 9 issues no total.
No Backend, diagnosticou e corrigiu divergência de schema entre produção e
código versionado, tratou vulnerabilidades de dependências, corrigiu drift
de infraestrutura como código numa variável de pagamento sensível, elevou
cobertura de testes unitários em 2 módulos e reforçou a cobertura de
branches do `PeopleController`, além de desabilitar a exposição pública do
Swagger em produção por padrão. No Frontend, centralizou máscaras de
telefone/CPF/CEP nos formulários do site e criou uma tela gamificada de
ranking de vendedores para a loja física.

**Grupo 3**, design e produto: estruturou as fundações do Design System
(tokens de cor, tipografia, espaçamento, raio, elevação e motion), criou a
biblioteca de componentes em variant sets, documentou os fluxos de
finalização de compra e pagamento para handoff, e organizou o quadro do
GitHub Projects usado pela equipe.

## Atividades detalhadas

Ordenado por data, depois trio, depois atividade; linhas sem data (n/d)
ficam ao final. Datas de commit são a evidência primária; PRs ainda não
mergeados estão marcados como tal (trabalho feito e demonstrável, faltando
só o merge).

| Trio | Atividade | Data |
|---|---|---|
| Equipe completa | Reunião no Teams: início da sprint | 05/09/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Integração contínua com o SonarCloud no Backend (`sonar-project.properties` + job de CI) | 05/09/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Integração contínua com o SonarCloud no Frontend (`sonar-project.properties` + job de CI) | 05/09/2026 |
| Grupo 3 (Ana Carvalho, Yzabella e Mateus) | Estruturação do Design System (tokens de cor, tipografia, espaçamento, raio, elevação e motion) | 05/09/2026 |
| Equipe completa | Reunião no Teams: comunicação entre os grupos para alinhar o que seria feito na sprint | 09/09/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Correções no workflow de métricas (caminho de saída do parser, diretório de trabalho, identificador de org/projeto na API do Sonar) | 10/09/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Workflow + script (`parser.py`) de coleta e exportação de métricas de qualidade brutas (files, functions, complexity, etc.), em Backend e Frontend | 10/09/2026 |
| Grupo 2 (Ana Aroeira, Gabriel e Leonardo) | Issue #173: Diagnóstico da divergência de schema entre produção e código versionado | 13/09/2026 |
| Grupo 2 (Ana Aroeira, Gabriel e Leonardo) | Issue #173: Elaboração, validação e aplicação de migration de correção em produção | 13/09/2026 |
| Equipe completa | Reunião no Teams: alinhamento da apresentação | 14/09/2026 |
| Grupo 2 (Ana Aroeira, Gabriel e Leonardo) | Issue #157: Diagnóstico de divergência entre schema do banco e migrations versionadas + decisão documentada de manter sincronização automática em dev | 14/09/2026 |
| Grupo 2 (Ana Aroeira, Gabriel e Leonardo) | Issue #160: Testes para os endpoints do `PeopleController`, elevando cobertura de branches do módulo de 67,85% para 75% e a global de 71,04% para 71,35% | 14/09/2026 |
| Grupo 2 (Ana Aroeira, Gabriel e Leonardo) | Issue #162: Correção de drift de IaC (`render.yaml`) na variável `PAYMENT_GATEWAY_PROVIDER` | 14/09/2026 |
| Grupo 2 (Ana Aroeira, Gabriel e Leonardo) | Issue #163: Swagger desabilitado em produção por padrão, reativável via `SWAGGER_PUBLIC` | 14/09/2026 *(PR #187 aberto)* |
| Grupo 2 (Ana Aroeira, Gabriel e Leonardo) | Issue #166: Diagnóstico de vulnerabilidades em dependências de produção | 14/09/2026 *(PR #189 aberto)* |
| Grupo 2 (Ana Aroeira, Gabriel e Leonardo) | Issue #166: Mitigação das vulnerabilidades de severidade alta e job de auditoria de dependências no CI | 14/09/2026 *(PR #189 aberto)* |
| Grupo 2 (Ana Aroeira, Gabriel e Leonardo) | Issue #168: 39 testes unitários novos para os módulos `reviews` e `sales-goals` | 14/09/2026 |
| Grupo 2 (Ana Aroeira, Gabriel e Leonardo) | Issue #172: Decisão documentada de não migrar TypeORM/TypeScript agora | 14/09/2026 |
| Grupo 2 (Ana Aroeira, Gabriel e Leonardo) | Issue #88: Máscaras de telefone, CPF e CEP centralizadas e aplicadas nos 6 formulários do site | 15/09/2026 *(PR #91 aberto)* |
| Grupo 2 (Ana Aroeira, Gabriel e Leonardo) | Issue #89: Tela de ranking gamificada para a loja física (`/painel/ranking-loja`), com rodízio de telas e confete ao bater meta | 15/09/2026 *(PR #90 aberto)* |
| Grupo 1 (Bruno, Eduardo e Márcio) | Definição, normalização e agregação analítica das métricas + aplicação Streamlit (dashboard de qualidade, testes, manutenibilidade, confiabilidade) | *n/d nos repos Backend/Frontend: aplicação separada* |
| Grupo 1 (Bruno, Eduardo e Márcio) | Refatoração da documentação, análise estática de links e CI de qualidade na documentação | *n/d nos repos Backend/Frontend: trabalho num repositório de documentação separado* |
| Grupo 3 (Ana Carvalho, Yzabella e Mateus) | Criação da biblioteca de componentes em variant sets | *n/d nos repos Backend/Frontend: trabalho em Figma* |
| Grupo 3 (Ana Carvalho, Yzabella e Mateus) | Criação e adaptação do GitHub Projects para controle de atividades | *n/d nos repos Backend/Frontend: configuração de projeto, não versionada em código* |
| Grupo 3 (Ana Carvalho, Yzabella e Mateus) | Desfechos de pagamento e documentação de handoff | *n/d nos repos Backend/Frontend: trabalho em Figma* |

## Evidências (Pull Requests)

| Issue | Repositório | PR | Status |
|---|---|---|---|
| #173 | Backend | [#181](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Backend/pull/181) | Mergeado |
| #166 | Backend | [#189](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Backend/pull/189) | Aberto |
| #157 | Backend | [#190](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Backend/pull/190) | Mergeado |
| #168 | Backend | [#188](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Backend/pull/188) | Mergeado |
| #162 | Backend | [#183](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Backend/pull/183) | Mergeado |
| #160 | Backend | [#184](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Backend/pull/184) | Mergeado |
| #172 | Backend | [#186](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Backend/pull/186) | Mergeado |
| #163 | Backend | [#187](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Backend/pull/187) | Aberto |
| #89 | Frontend | [#90](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Frontend/pull/90) | Aberto |
| #88 | Frontend | [#91](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Frontend/pull/91) | Aberto |

## Notas de apuração

- **Grupo 2** é o único totalmente rastreável pelo histórico de commits: todas
  as 12 linhas batem com commits/PRs reais nos dois repositórios.
- **Datas de PRs ainda abertos** (#189, #187, #91, #90) são a data do último
  commit relevante na branch, não de merge: o trabalho está feito e
  demonstrável, só falta o merge.
- **Grupo 1**: 4 das 6 atividades do slide são rastreáveis (Sonar + métricas);
  as outras 2 (documentação, dashboard Streamlit) vivem fora de
  `MarketPlace-Backend`/`MarketPlace-Frontend`.
- **Grupo 3**: nenhuma atividade aparece no histórico de código dos dois
  repos (é trabalho de design em Figma e gestão de projeto, coerente com o
  conteúdo do slide, sem menção a issue/PR). A data da estruturação do
  Design System foi ajustada para o início da sprint (05/09/2026) a pedido
  da equipe.

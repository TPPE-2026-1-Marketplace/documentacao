# DK Fashion - Sprint 2 - Documento de Entrega

Documento final de entrega da Sprint 2 do projeto DK Fashion (disciplina
GCES). Consolida atividades esperadas x realizadas dos 3 trios, com
evidência real extraída do histórico de commits e Pull Requests de
`MarketPlace-Backend` e `MarketPlace-Frontend` (org TPPE-2026-1-Marketplace),
cruzado com o conteúdo do slide `GCES - Sprint 2 .pdf`.

## Visão geral da sprint

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| Squad            | 9 integrantes, em 3 trios                                                             |
| Período          | 15/09/2026 a 05/10/2026                                                               |
| Repositórios     | `MarketPlace-Backend`, `MarketPlace-Frontend`                                         |
| Reuniões (Teams) | 15/09 (início), 30/09 (alinhamento entre grupos), 05/10 (alinhamento da apresentação) |

## Equipe

| Trio    | Integrantes                                           |
| ------- | ----------------------------------------------------- |
| Grupo 1 | Bruno Bragança, Eduardo Sandes, Marcio Costa          |
| Grupo 2 | Ana Luiza Aroeira, Gabriel Anjos, Leonardo Sauma      |
| Grupo 3 | Ana Luiza Carvalho, Yzabella Miranda, Mateus Consorte |

## Resumo por trio

**Grupo 1**, incremento do dashboard de análise de qualidade dos repositórios, trazendo novas métricas como: falhas de teste, erros de teste e tempo de teste; bem como a melhora da apresentação visual do dashboard com a identidade do projeto. Além disso foi feita a melhoria da qualidade do Frontend através da implementação de testes automatizados (84% de cobertura). Também foram implementadas novas páginas e componentes do Frontend, com base nos protótipos previamente validados, contemplando os fluxos de carrinho, checkout e confirmação de pedido.

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

| Trio                              | Atividade                                                                                                     | Data       |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------- |
| Equipe completa                   | Reunião presencial: início da sprint                                                                          | 05/09/2026 |
| Equipe completa                   | Reunião no Teams: comunicação entre os grupos para alinhar o que seria feito na sprint                        | 30/09/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Adição das seguintes métricas no dashboard de qualidade: falhas de teste, erros de teste e tempo de teste     | 03/10/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Melhora da estética do dashboard de qualidade                                                                 | 03/10/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Implementação dos testes automatizados no front                                                               | 03/10/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Correções no workflow de métricas (mudança para executar somente após a conclusão da análise do Sonar)        | 03/10/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Implementação dos componentes do carrinho                                                                     | 05/10/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Implementação da infraestrutura de testes das novas páginas e componentes                                     | 05/10/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Implementação dos testes unitários dos componentes do carrinho                                                | 05/10/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Integração da execução de testes automatizados ao workflow de CI                                              | 05/10/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Implementação da nova página de carrinho                                                                      | 05/10/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Implementação da nova página de checkout                                                                      | 05/10/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Implementação da nova página de confirmação do pedido e integração com o retorno do gateway de pagamento      | 05/10/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Atualização dos testes automatizados de Selenium para os fluxos de carrinho, checkout e confirmação de pedido | 05/10/2026 |
| Grupo 1 (Bruno, Eduardo e Márcio) | Implementação dos componentes de interface base e ajustes nos tokens do design system conforme o Figma        | 05/10/2026 |
| Equipe completa                   | Reunião no Teams: alinhamento da apresentação                                                                 | 05/10/2026 |

## Evidências (Pull Requests)

| Issue | Repositório | PR                                                                               | Status   |
| ----- | ----------- | -------------------------------------------------------------------------------- | -------- |
| #129  | Frontend    | [#124](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Frontend/pull/124) | Mergeado |
| #129  | Frontend    | [#125](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Frontend/pull/125) | Mergeado |
| #130  | Frontend    | [#126](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Frontend/pull/126) | Mergeado |
| #72   | Frontend    | [#127](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Frontend/pull/127) | Mergeado |
| #72   | Frontend    | [#128](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Frontend/pull/128) | Mergeado |
| #203  | Backend     | [#128](https://github.com/TPPE-2026-1-Marketplace/MarketPlace-Backend/pull/193)  | Mergeado |

## Notas de apuração

- **Grupo 2** é o único totalmente rastreável pelo histórico de commits: todas
  as 12 linhas batem com commits/PRs reais nos dois repositórios.

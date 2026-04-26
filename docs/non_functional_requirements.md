# Requisitos Não Funcionais

## Lista de Requisitos Não Funcionais

### RNF01 - Sincronização de estoque em tempo real
Sincronizar o saldo de estoque em tempo real entre a loja física e a plataforma de e-commerce.

**Histórias relacionadas:**

- [US01 - Registrar produto](user_history/catalogo_modelagem.md#us01-registrar-produto)
- [US23 - Registrar histórico de alteração no estoque](user_history/estoque_loja_fisica_operacao.md#us23-registrar-historico-de-alteracao-no-estoque)
- [US24 - Registrar compras presenciais](user_history/estoque_loja_fisica_operacao.md#us24-registrar-compras-presenciais)

**Observações:**

- Possível solução: separar estoque presencial e estoque digital
- Nem todos os modelos físicos serão disponibilizados no digital
- Caso exista maior demanda em um canal do que no outro, deve haver um mecanismo de comunicação ou balanceamento

### RNF02 - Regra de exibição de produtos em destaque
Limitar a exibição de produtos em destaque na página inicial a exatamente 8 itens.

**Histórias relacionadas:**

- [US03 - Página inicial](user_history/busca_navegacao_atendimento.md#us03-pagina-inicial)
- [US04 - Filtrar produtos por critérios de busca](user_history/busca_navegacao_atendimento.md#us04-filtrar-produtos-por-criterios-de-busca)
- [US10 - Incluir redirecionamento para o WhatsApp](user_history/busca_navegacao_atendimento.md#us10-incluir-redirecionamento-para-o-whatsapp)

### RNF03 - Integração segura de pagamentos no site
Integrar o sistema com as APIs de pagamento das adquirentes InfinitePay ou HyperCast, garantindo que o pagamento seja realizado dentro da plataforma.

**Histórias relacionadas:**

- [US16 - Oferecer múltiplas formas de pagamento](user_history/compra_pagamento_entrega.md#us16-oferecer-multiplas-formas-de-pagamento)
- [US17 - Calcular prazo e custo de frete](user_history/compra_pagamento_entrega.md#us17-calcular-prazo-e-custo-de-frete)
- [US18 - Inserir código de rastreamento manualmente](user_history/compra_pagamento_entrega.md#us18-inserir-codigo-de-rastreamento-manualmente)

### RNF04 - Integração com emissão de NF-e
Integrar o sistema com um serviço de emissão de Nota Fiscal Eletrônica (NF-e) e Certificado Digital.

**Histórias relacionadas:**

- [US15 - Retirar pedido na loja física](user_history/compra_pagamento_entrega.md#us15-retirar-pedido-na-loja-fisica)
- [US16 - Oferecer múltiplas formas de pagamento](user_history/compra_pagamento_entrega.md#us16-oferecer-multiplas-formas-de-pagamento)
- [US18 - Inserir código de rastreamento manualmente](user_history/compra_pagamento_entrega.md#us18-inserir-codigo-de-rastreamento-manualmente)

### RNF05 - Emissão de crédito interno para devoluções
Emitir crédito interno, no formato de cupom de troca, para clientes em casos de devolução de mercadoria.

**Histórias relacionadas:**

- [US13 - Gerenciar cupons de desconto](user_history/clientes_crm_marketing.md#us13-gerenciar-cupons-de-desconto)
- [US14 - Gerenciar cupons de desconto para parceiros](user_history/clientes_crm_marketing.md#us14-gerenciar-cupons-de-desconto-para-parceiros)

## Regras de Negócio

### RN01 - Seleção de grade de tamanhos no vestuário virtual
Disponibilizar a grade de tamanhos padrão para seleção no vestiário virtual.

**História relacionada:**

- [US01 - Registrar produto](user_history/catalogo_modelagem.md#us01-registrar-produto)

### RN02 - Limite de itens em destaque na página inicial
Aplicar a regra de 8 itens na vitrine principal.

**História relacionada:**

- Item originalmente levantado como US09 e posteriormente reclassificado como requisito não funcional

### RN03 - Comissão automática por venda vinculada
Calcular automaticamente a comissão de 2,5% sobre o valor acumulado no mês para o vendedor vinculado.

**História relacionada:**

- [US20 - Calcular comissão do vendedor automaticamente](user_history/estoque_loja_fisica_operacao.md#us20-calcular-comissao-do-vendedor-automaticamente)

## Histórico de Versionamento

| Versão | Autor | Resumo | Data |
| --------------- | --------------- | --------------- | --------------- |
| `1.0` | [Ana Luiza](https://github.com/Ana-Luiza-SC), [Gabriel](https://github.com/), [Leo](https://github.com/leohssjr), [Mateus](https://github.com/MVConsorte) e [Yzabella](https://github.com/redjsun) | Documentação inicial | 28/03/2026 |
| `1.1` | [Pablo](https://github.com/Pabloserrapxx) | Atualização e incremento de Requisitos não Funcionais | 29/03/2026 |
| `1.2` | [Bruno Bragança](https://github.com/BrunoBReis) | Verificação e Atualização com incremento de Regras de negócio | 29/03/2026 |
| `1.3` | [Bruno Bragança](https://github.com/BrunoBReis) | Reclassificação, revisão e relacionamento entre RNFs e histórias de usuário | 06/04/2026 |
| `1.4` | [Pablo](https://github.com/Pabloserrapxx) | Atualização das histórias de usuário | 26/04/2026 |

# Requisitos Não Funcionais

## Lista de Requisitos Não Funcionais

### RNF01 - Sincronização de estoque em tempo real
Sincronizar o saldo de estoque em tempo real entre a loja física e a plataforma de e-commerce.

**Histórias relacionadas:**

- [US05 - Integrar leitor de código de barras ao PDV físico](user_history/estoque_loja_fisica_operacao.md#us05-integrar-leitor-de-codigo-de-barras-ao-pdv-fisico)
- [US14 - Restringir ajuste manual de estoque ao gerente](user_history/estoque_loja_fisica_operacao.md#us14-restringir-ajuste-manual-de-estoque-ao-gerente)
- [US28 - Registrar log de auditoria de estoque](user_history/estoque_loja_fisica_operacao.md#us28-registrar-log-de-auditoria-de-estoque)
- [US30 - Realizar carga inicial de estoque](user_history/estoque_loja_fisica_operacao.md#us30-realizar-carga-inicial-de-estoque)

**Observações:**
- Possível solução: separar estoque presencial e estoque digital
- Nem todos os modelos físicos serão disponibilizados no digital
- Caso exista maior demanda em um canal do que no outro, deve haver um mecanismo de comunicação ou balanceamento

### RNF02 - Regra de exibição de produtos em destaque
Limitar a exibição de produtos em destaque na página inicial a exatamente 8 itens.

**Histórias relacionadas:**

- [US06 - Filtrar produtos por critérios de busca](user_history/busca_navegacao_atendimento.md#us06-filtrar-produtos-por-criterios-de-busca)
- [US07 - Aplicar zoom nas fotos dos produtos](user_history/busca_navegacao_atendimento.md#us07-aplicar-zoom-nas-fotos-dos-produtos)
- [US24 - Incluir suporte via WhatsApp com dados do produto](user_history/busca_navegacao_atendimento.md#us24-incluir-suporte-via-whatsapp-com-dados-do-produto)

### RNF03 - Integração segura de pagamentos no site
Integrar o sistema com as APIs de pagamento das adquirentes InfinitePay ou HyperCast, garantindo que o pagamento seja realizado dentro da plataforma.

**Histórias relacionadas:**

- [US15 - Oferecer múltiplas formas de pagamento](user_history/compra_pagamento_entrega.md#us15-oferecer-multiplas-formas-de-pagamento)
- [US16 - Calcular prazo e custo de frete](user_history/compra_pagamento_entrega.md#us16-calcular-prazo-e-custo-de-frete)
- [US17 - Inserir código de rastreamento manualmente](user_history/compra_pagamento_entrega.md#us17-inserir-codigo-de-rastreamento-manualmente)
- [US27 - Implementar checkout simplificado em página única](user_history/compra_pagamento_entrega.md#us27-implementar-checkout-simplificado-em-pagina-unica)

### RNF04 - Integração com emissão de NF-e
Integrar o sistema com um serviço de emissão de Nota Fiscal Eletrônica (NF-e) e Certificado Digital.

**Histórias relacionadas:**

- [US08 - Retirar pedido na loja física](user_history/compra_pagamento_entrega.md#us08-retirar-pedido-na-loja-fisica)
- [US09 - Validar retirada presencial com código de verificação](user_history/compra_pagamento_entrega.md#us09-validar-retirada-presencial-com-codigo-de-verificacao)
- [US15 - Oferecer múltiplas formas de pagamento](user_history/compra_pagamento_entrega.md#us15-oferecer-multiplas-formas-de-pagamento)

### RNF05 - Emissão de crédito interno para devoluções
Emitir crédito interno, no formato de cupom de troca, para clientes em casos de devolução de mercadoria.

**Histórias relacionadas:**

- [US18 - Gerar cupons de desconto por campanha](user_history/clientes_crm_marketing.md#us18-gerar-cupons-de-desconto-por-campanha)

## Regras de Negócio

### RN01 - Seleção de grade de tamanhos no vestuário virtual
Disponibilizar a grade de tamanhos padrão para seleção no vestiário virtual.

**História relacionada:**

- [US02 - Selecionar tamanho padrão no vestuário virtual](user_history/catalogo_modelagem.md#us02-selecionar-tamanho-padrao-no-vestuario-virtual)

### RN02 - Limite de itens em destaque na página inicial
Aplicar a regra de 8 itens na vitrine principal.

**História relacionada:**

- Item originalmente levantado como US09 e posteriormente reclassificado como requisito não funcional

### RN03 - Comissão automática por venda vinculada
Calcular automaticamente a comissão de 2,5% sobre o valor da venda para o vendedor vinculado.

**História relacionada:**

- [US12 - Calcular comissão do vendedor automaticamente](user_history/estoque_loja_fisica_operacao.md#us12-calcular-comissao-do-vendedor-automaticamente)

## Histórico de Versionamento

| Versão | Autor | Resumo | Data |
| --------------- | --------------- | --------------- | --------------- |
| `1.0` | [Ana Luiza](https://github.com/Ana-Luiza-SC), [Gabriel](https://github.com/), [Leo](https://github.com/leohssjr), [Mateus](https://github.com/MVConsorte) e [Yzabella](https://github.com/redjsun) | Documentação inicial | 28/03/2026 |
| `1.1` | [Pablo](https://github.com/Pabloserrapxx) | Atualização e incremento de Requisitos não Funcionais | 29/03/2026 |
  | `1.2` | [Bruno Bragança](https://github.com/BrunoBReis) | Verificação e Atualização com incremento de Regras de negócio | 29/03/2026 |

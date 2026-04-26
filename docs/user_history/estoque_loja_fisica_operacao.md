# Estoque, Loja Física e Operação

## US19 - Vincular vendedor a cada transação
**Como** caixa,  
**quero** poder associar o vendedor da venda,  
**para que** as vendas de cada vendedor sejam rastreadas e as comissões possam ser apuradas corretamente.

### Finalidade
- Permitir a vinculação de um vendedor específico a cada transação
- Utilizar essa vinculação para auditoria e cálculo de comissão

## US20 - Calcular comissão do vendedor automaticamente
**Como** administrador,  
**quero** poder visualizar as comissões que devo pagar,  
**para que** eu não precise calcular manualmente a comissão de cada vendedor no fechamento da folha de pagamento.

### Regra de negócio
Calcular automaticamente a comissão de 2,5% sobre o valor acumulado no mês para o vendedor vinculado.

## US22 - Definir níveis de acesso por perfil
**Como** administrador,  
**quero** que existam diferentes níveis de acesso ao sistema,  
**para que** os vendedores não tenham acesso a áreas sensíveis de gestão do negócio.

### Perfis
- Caixa: acesso ao sistema de vendas para registrar compras na loja física e associar vendedores.
- Vendedor: mesmo nível do caixa, com participação no ranking de vendas e comissão.
- Gerente: mesmo nível do vendedor, com controle de estoque e acesso a dashboards gerenciais.
- Administrador: mesmo nível do gerente, com gestão de funcionários, níveis de acesso, cupons e dados de clientes.

## US23 - Registrar histórico de alteração no estoque
**Como** administrador,  
**quero** visualizar um histórico com usuário, data, campos alterados com antes e depois e motivo opcional,  
**para que** eu tenha rastreabilidade total sobre alterações em dados de estoque.

## US24 - Registrar compras presenciais
**Como** caixa,  
**quero** registrar compras realizadas na loja física,  
**para que** gerente e administrador acompanhem vendas e os vendedores recebam suas comissões.

### Regras de negócio
- Cada venda presencial deve ser associada a apenas um vendedor.
- A cada compra registrada, o estoque deve ser decrementado conforme a quantidade vendida.

## Histórico de Versionamento

| Versão | Autor | Resumo | Data |
| --------------- | --------------- | --------------- | --------------- |
| `1.0` | [Ana Luiza](https://github.com/Ana-Luiza-SC), [Gabriel](https://github.com/), [Leo](https://github.com/leohssjr), [Mateus](https://github.com/MVConsorte) e [Yzabella](https://github.com/redjsun) | Documentação inicial | 28/03/2026 |
| `1.1` | [Pablo](https://github.com/Pabloserrapxx) | Atualização e incremento de Requisitos não Funcionais | 29/03/2026 |
| `1.2` | [Bruno Bragança](https://github.com/BrunoBReis) | Verificação e Atualização com incremento de Regras de negócio | 29/03/2026 |
| `1.3` | [Bruno Bragança](https://github.com/BrunoBReis) | Reorganização, renumeração e refinamento das histórias de usuário | 06/04/2026 |
| `1.4` | [Pablo](https://github.com/Pabloserrapxx) | Substituição das histórias por novo escopo de operação, estoque e comissões | 26/04/2026 |

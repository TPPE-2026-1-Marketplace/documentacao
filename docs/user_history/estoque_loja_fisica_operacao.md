# Estoque, Loja Física e Operação

## US05 - Registrar movimentações de estoque com rastreabilidade
**Como** vendedor,  
**quero** utilizar o código de barras para registrar automaticamente as movimentações de estoque, com identificação do usuário, data e motivo,  
**para que** o estoque seja atualizado corretamente e cada movimentação possa ser auditada.

## US11 - Vincular vendedor a cada transação
**Como** caixa da loja,  
**quero** poder associar o vendedor da venda,  
**para que** as vendas de cada vendedor sejam rastreadas e as comissões possam ser apuradas corretamente.

### Finalidade
- Permitir a vinculação de um vendedor específico a cada transação
- Utilizar essa vinculação para auditoria e cálculo de comissão

## US12 - Calcular comissão do vendedor automaticamente
**Como** administrador da loja,  
**quero** poder visualizar as comissões que devo pagar,  
**para que** eu não precise calcular manualmente a comissão de cada vendedor no fechamento da folha de pagamento.

### Regra de negócio
Calcular automaticamente a comissão de 2,5% sobre o valor da venda para o vendedor vinculado.

## US13 - Definir níveis de acesso por perfil
**Como** administrador da loja,  
**quero** que existam diferentes níveis de acesso ao sistema,  
**para que** os vendedores não tenham acesso a áreas sensíveis de gestão do negócio.

### Perfis
- Vendedor
- Gerente
- Administrador

## US14 - Restringir ajuste manual de estoque ao gerente
**Como** administrador da loja,  
**quero** que apenas o gerente da loja possa adicionar ou remover produtos do e-commerce,  
**para que** a manutenção do sistema seja realizada apenas por pessoas autorizadas.

### Regra de acesso
Restringir as funções de ajuste manual de estoque, como adição e exclusão, exclusivamente ao perfil de gerente.

## US28 - Realizar carga inicial de estoque
**Como** gerente de operações,  
**quero** uma interface para realizar a carga inicial e a digitalização do acervo atual,  
**para que** eu possa cadastrar todo o estoque físico no sistema de forma organizada no início da operação.

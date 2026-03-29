# Estoque, Loja Física e Operação

## US05 - Integrar leitor de código de barras ao PDV físico
**Como** vendedor,  
**quero** poder utilizar o código de barras,  
**para que** possa realizar baixa automaticamente no estoque no PDV físico.

## US11 - Vincular vendedor a cada transação
**Como** caixa da loja,  
**quero** poder associar o vendedor da venda,  
**para que** os lojistas possam receber suas comissões e as vendas de cada um sejam rastreadas.

### Finalidade
- Permitir a vinculação de um vendedor específico a cada transação
- Utilizar essa vinculação para auditoria e cálculo de comissão

## US12 - Calcular comissão do vendedor automaticamente
**Como** administrador da loja,  
**quero** poder visualizar as comissões que devo pagar,  
**para que** eu não precise calcular manualmente a comissão de cada lojista no fechamento da folha de pagamento.

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
**quero** que apenas o gerente da loja possa cadastrar ou retirar produtos do e-commerce,  
**para que** eu mantenha a segurança e a manutenção do sistema.

### Regra de acesso
Restringir as funções de ajuste manual de estoque, como adição e exclusão, exclusivamente ao perfil de gerente.

## US28 - Registrar log de auditoria de estoque
**Como** administrador ou gerente,  
**quero** que o sistema registre automaticamente um log com usuário, data e motivo para cada movimentação de estoque,  
**para que** eu tenha total rastreabilidade sobre as alterações e possa auditar possíveis divergências.

## US30 - Realizar carga inicial de estoque
**Como** gerente de operações,  
**quero** uma interface para realizar a carga inicial e a digitalização do acervo atual,  
**para que** eu possa cadastrar todo o estoque físico no sistema de forma organizada no início da operação.

## Histórico de Versionamento

| Versão | Autor | Resumo | Data |
| --------------- | --------------- | --------------- | --------------- |
| `1.0` | [Ana Luiza](https://github.com/Ana-Luiza-SC), [Gabriel](https://github.com/), [Leo](https://github.com/leohssjr), [Mateus](https://github.com/MVConsorte) e [Yzabella](https://github.com/redjsun) | Documentação inicial | 28/03/2026 |
| `1.1` | [Pablo](https://github.com/Pabloserrapxx) | Atualização e incremento de Requisitos não Funcionais | 29/03/2026 |
| `1.2` | [Bruno Bragança](https://github.com/BrunoBReis) | Verificação e Atualização com incremento de Regras de negócio | 29/03/2026 |

# Gitflow do Projeto

Este documento define o fluxo de trabalho Git adotado no projeto, com foco em previsibilidade, integração contínua e segurança no processo de release.

## Objetivos do fluxo

- manter a `main` sempre estável e pronta para produção;
- usar a `dev` como branch principal de integração do time;
- desenvolver cada issue de forma isolada, sem perder rastreabilidade;
- exigir validações automáticas antes de qualquer merge;
- garantir que o deploy de produção aconteça a partir da `main`.

## Branches principais

### `main`

- representa o código em produção;
- deve permanecer estável;
- só recebe mudanças aprovadas e validadas;
- possui CI/CD rigoroso;
- o pipeline dessa branch deve executar o deploy.

### `dev`

- representa o ambiente de integração do time;
- concentra o trabalho do ciclo atual;
- recebe as implementações das issues;
- possui CI/CD rigoroso;
- deve estar sempre em condição utilizável para homologação interna.

## Branches de trabalho

Cada issue deve ser desenvolvida em uma branch própria, criada a partir da `dev`.

Formato recomendado:

```bash
git checkout dev
git pull origin dev
git checkout -b feat/nome-curto-da-issue
```

Ou, em caso de correção:

```bash
git checkout -b fix/nome-curto-da-issue
```

### Regras para issues

- uma issue representa parte de uma história de usuário, e não a história completa;
- cada issue deve ter escopo pequeno, claro e validável;
- a implementação da issue deve ser integrada na `dev`;
- o merge de uma issue não deve quebrar a `dev`;
- a issue deve estar vinculada ao Pull Request correspondente.

## Fluxo de desenvolvimento

O fluxo padrão será:

1. criar uma issue a partir do backlog ou da decomposição de uma história de usuário;
2. criar uma branch de trabalho derivada da `dev`;
3. implementar a mudança e adicionar ou atualizar testes;
4. abrir um Pull Request para `dev`;
5. executar o CI da branch e do PR;
6. realizar revisão de código;
7. fazer merge na `dev` apenas após aprovação e pipeline verde.

## Regras de CI/CD

### Para `dev`

O pipeline da `dev` deve ser rígido o suficiente para impedir a degradação contínua do projeto. Recomenda-se validar:

- lint e formatação;
- testes unitários;
- testes de integração, quando existirem;
- cobertura mínima, se o time definir esse critério;
- build da aplicação;
- verificações de segurança e dependências, quando possível.

### Para `main`

O pipeline da `main` deve ser ainda mais restritivo, pois essa branch representa produção. Recomenda-se executar:

- todas as validações da `dev`;
- validações finais de empacotamento ou publicação;
- geração de artefatos de release;
- deploy automático ou controlado para o ambiente de produção.

## Processo de release

Ao final de um ciclo de desenvolvimento, deve ocorrer a release do conteúdo estabilizado na `dev`.

Fluxo esperado:

1. congelar novas entradas na release, priorizando estabilização;
2. garantir que a `dev` esteja com pipeline verde;
3. abrir um Pull Request de `dev` para `main`;
4. executar revisão final e validações da `main`;
5. fazer o merge em `main`;
6. disparar o deploy a partir da `main`;
7. criar a tag da versão da release.

Exemplo de versionamento:

```bash
git checkout main
git pull origin main
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

## Hotfixes

Embora o fluxo principal ocorra pela `dev`, é importante prever correções urgentes em produção.

Nesses casos:

- a branch de hotfix deve sair da `main`;
- a correção deve passar pelo CI/CD da `main`;
- após o merge na `main`, a correção deve ser replicada para a `dev` para evitar divergência entre as branches.

Formato recomendado:

```bash
git checkout main
git pull origin main
git checkout -b hotfix/descricao-curta
```

## Regras de merge

- evitar `push` direto em `main` e `dev`;
- proteger as branches `main` e `dev`;
- exigir Pull Request para qualquer mudança nessas branches;
- exigir pipeline aprovado antes do merge;
- exigir ao menos uma revisão de outro integrante do time;
- preferir squash merge ou merge commit conforme a estratégia definida pelo time, mas usar o padrão de forma consistente.

## Responsabilidades do time

- decompor histórias de usuário em issues pequenas e rastreáveis;
- manter as issues atualizadas com contexto técnico e critérios de aceite;
- relacionar commits e PRs com as issues;
- atualizar a documentação quando o fluxo ou o processo de release mudar.


## Histórico de Versionamento

| Versão | Autor | Resumo | Data |
| --------------- | --------------- | --------------- | --------------- |
| `1.0` | [Bruno Bragança](https://github.com/BrunoBReis) | Criação da página de definição do gitflow do projeto | 06/04/2026 |

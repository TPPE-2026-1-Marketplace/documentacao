# Contributing Guidelines

Obrigado por considerar contribuir com este projeto. Este documento define as diretrizes para garantir consistência, qualidade e colaboração eficiente.

---

## Fluxo de contribuição

1. Faça um fork do repositório
2. Crie uma branch para sua feature ou correção:

   ```bash
   git checkout -b feat/nome-da-feature
   ```
3. Realize suas alterações
4. Faça commits seguindo o padrão definido
5. Envie para o seu fork:

   ```bash
   git push origin feat/nome-da-feature
   ```
6. Abra um Pull Request (PR)


## Padrão de commits (OBRIGATÓRIO)

Este projeto utiliza o padrão **Conventional Commits**.

Formato obrigatório:

```
<type>(<optional scope>): <description>

[optional body]

[optional footer]
```

Esse padrão melhora legibilidade, histórico e permite automação como geração de changelog e versionamento semântico.


### Estrutura

* **type** → tipo da mudança (obrigatório)
* **scope** → módulo afetado (opcional)
* **description** → descrição curta e clara
* **body** → explicação detalhada (opcional)
* **footer** → breaking changes / issues (opcional)


### Tipos de commit

Use os seguintes tipos:

| Tipo       | Descrição                             |
| ---------- | ------------------------------------- |
| `feat`     | Nova funcionalidade                   |
| `fix`      | Correção de bug                       |
| `docs`     | Alterações na documentação            |
| `style`    | Formatação, sem mudança de lógica     |
| `refactor` | Refatoração sem alterar comportamento |
| `perf`     | Melhoria de performance               |
| `test`     | Adição ou ajuste de testes            |
| `build`    | Build, dependências                   |
| `ci`       | Integração contínua                   |
| `chore`    | Tarefas gerais (ex: configs)          |
| `revert`   | Reversão de commit                    |

Esses tipos seguem o padrão amplamente adotado na especificação.

---

### Exemplos

```bash
feat(auth): add login with JWT

fix(api): resolve timeout issue

docs(readme): update installation instructions

refactor(core): simplify validation logic

perf(database): optimize query execution

chore: update dependencies
```


### Regras importantes

* Use **inglês** nos commits
* Use verbo no **imperativo** (ex: "add", "fix", "update")
* Máximo de ~72 caracteres na descrição
* Evite commits genéricos como:

  * `update code`
  * `fix bug`
* Prefira commits pequenos e focados


## Breaking Changes

Para mudanças incompatíveis:

```bash
feat(api)!: change authentication flow
```

Ou no footer:

```
BREAKING CHANGE: authentication now requires token
```


## Pull Requests

* Descreva claramente o objetivo
* Relacione issues (se houver)
* Inclua evidências (logs, prints, testes)
* Garanta que o código compila/testa corretamente


## Testes

* Novas features devem incluir testes
* Bugs corrigidos devem ter testes associados
* Evite quebrar testes existentes


## Padrões de código

* Siga o padrão do projeto
* Código legível > código complexo
* Evite duplicação


## Boas práticas

* Não commitar:

  * `.env`
  * segredos / tokens
* Use `.gitignore` corretamente
* Sempre atualize documentação quando necessário


## Código de conduta

* Seja respeitoso
* Feedback construtivo
* Colaboração acima de ego


## Observação final

Commits padronizados tornam o histórico **legível, automatizável e escalável**, sendo essenciais em projetos colaborativos.

# DK Fashion - Documentação

Repositório da documentação do projeto **DK Fashion**.

## Sobre a documentação

Esta documentação centraliza os principais artefatos da primeira entrega do projeto, incluindo:

- backlog do produto;
- requisitos não funcionais;
- arquitetura do projeto;
- modelagem do banco de dados;
- conteinerização do ambiente

## Como executar

O fluxo oficial do projeto é via Docker: não é necessário criar ambiente
virtual nem instalar Python/MkDocs na máquina. Todos os targets do `Makefile`
rodam em container.

1. Suba a documentação:

```bash
make serve

# ou

make serve-background # sobe como Daemon
```

1. Acesse:

```text
http://localhost:8000
```

1. Para parar o container:

```bash
make stop
```

Para gerar o site estático em `./site`:

```bash
make build
```

> Rodar o MkDocs direto na máquina (com `pip install -r requirements.txt`)
> continua funcionando, mas não é mais coberto pelo `Makefile`.

## Controle de qualidade

A documentação tem dois checks automáticos, executados no CI a cada Pull
Request (workflow `docs quality`) e disponíveis localmente:

| Comando | O que faz |
| --- | --- |
| `make lint-md` | Valida estilo e consistência do Markdown com o `markdownlint-cli2` |
| `make lint-md-fix` | Corrige automaticamente o que for corrigível (espaçamento, listas, tabelas) |
| `make check-links` | Roda `mkdocs build --strict` e varre o HTML gerado com o `LinkChecker` |
| `make check-links-extern` | Igual ao anterior, incluindo links externos (depende de rede) |
| `make quality` | Executa `lint-md` + `check-links` |

## Apresentações de sprint

Os slides são gerados com [Marp](https://marp.app/) a partir dos arquivos em
`slides/`, também em container:

```bash
cp slides/template.md slides/01.md   # edite o conteúdo da sprint
make slides                          # HTML em slides/dist/
make slides-pdf                      # HTML + PDF
```

O script `scripts/build-slides.sh` aceita um deck específico
(`./scripts/build-slides.sh slides/01.md`) e o formato `--pptx`. A saída em
`slides/dist/` não é versionada.

As regras do lint ficam em `.markdownlint-cli2.jsonc` e a configuração do
LinkChecker em `.linkcheckerrc`. A checagem de links externos roda no CI de
forma informativa: ela não bloqueia o merge, porque depende de serviços de
terceiros.

## Como funciona a conteinerização

- o `Dockerfile` tem dois estágios: `docs` (MkDocs, a partir do
  `requirements.txt`) e `quality` (adiciona o LinkChecker, do
  `requirements-dev.txt`);
- o `compose.yaml` publica a porta `8000` e monta o diretório do projeto em `/app`;
- esse volume permite editar arquivos em `docs/` e ver as mudanças com hot reload no MkDocs;
- os serviços `lint-md` e `check-links` ficam no profile `quality`, então não
  sobem junto com `make serve` — são executados sob demanda;
- se `requirements.txt` mudar, execute novamente `make serve` (ele reconstrói a imagem).

## Padrão de commits

Os commits seguem [Conventional Commits](https://www.conventionalcommits.org/pt-br/)
(`feat:`, `fix:`, `docs:`, `ci:`, `style:`...), com o assunto em português e no
imperativo.

Como Bruno, Eduardo e Márcio trabalham em par/trio, o repositório tem um hook
que preenche os `Co-authored-by` sozinho: quem commita entra como autor e os
outros dois entram como co-autores. Ative uma vez por clone:

```bash
make hooks   # equivale a: git config core.hooksPath .githooks
```

Feito isso, um `git commit -m "feat: nova página"` do Márcio vira:

```text
feat: nova página

Co-authored-by: Bruno Braganca <brunobragancadosreis@gmail.com>
Co-authored-by: Eduardo Sandes <eduardo.sandes6@gmail.com>
```

Detalhes:

- o hook (`.githooks/commit-msg`) identifica a pessoa pelo `user.email` do
  clone, então cada um precisa ter o `git config user.email` correto — o
  endereço `@users.noreply.github.com` também é reconhecido;
- commits de quem não é do trio passam sem alteração;
- co-autor escrito à mão não é duplicado;
- `git commit --no-verify` pula o hook.

## Estrutura do repositório

```text
.
|-- .githooks/
|   `-- commit-msg
|-- docs/
|   |-- index.md
|   |-- contributing_guidelines.md
|   |-- user_history.md
|   |-- non_functional_requirements.md
|   `-- user_history/
|-- scripts/
|   `-- check-links.sh
|-- mkdocs.yml
|-- Dockerfile
|-- compose.yaml
|-- requirements.txt
|-- requirements-dev.txt
|-- .markdownlint-cli2.jsonc
|-- .linkcheckerrc
|-- Makefile
`-- README.md
```

## Equipe TPPE (26.1)

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Ana-Luiza-SC">
        <img src="https://github.com/Ana-Luiza-SC.png?size=160" width="120" alt="Foto de Ana Luiza"><br>
        <strong>Ana Luiza</strong>
      </a>
      <br>
      <a href="https://github.com/Ana-Luiza-SC">github.com/Ana-Luiza-SC</a>
    </td>
    <td align="center">
      <a href="https://github.com/SAnjos3">
        <img src="https://github.com/SAnjos3.png?size=160" width="120" alt="Foto de Gabriel"><br>
        <strong>Gabriel</strong>
      </a>
      <br>
      <a href="https://github.com/SAnjos3">github.com/SAnjos3</a>
    </td>
    <td align="center">
      <a href="https://github.com/leohssjr">
        <img src="https://github.com/leohssjr.png?size=160" width="120" alt="Foto de Leo"><br>
        <strong>Leo</strong>
      </a>
      <br>
      <a href="https://github.com/leohssjr">github.com/leohssjr</a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/MVConsorte">
        <img src="https://github.com/MVConsorte.png?size=160" width="120" alt="Foto de Mateus"><br>
        <strong>Mateus</strong>
      </a>
      <br>
      <a href="https://github.com/MVConsorte">github.com/MVConsorte</a>
    </td>
    <td align="center">
      <a href="https://github.com/redjsun">
        <img src="https://github.com/redjsun.png?size=160" width="120" alt="Foto de Yzabella"><br>
        <strong>Yzabella</strong>
      </a>
      <br>
      <a href="https://github.com/redjsun">github.com/redjsun</a>
    </td>
    <td align="center">
      <a href="https://github.com/Pabloserrapxx">
        <img src="https://github.com/Pabloserrapxx.png?size=160" width="120" alt="Foto de Pablo"><br>
        <strong>Pablo</strong>
      </a>
      <br>
      <a href="https://github.com/Pabloserrapxx">github.com/Pabloserrapxx</a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/BrunoBReis">
        <img src="https://github.com/BrunoBReis.png?size=160" width="120" alt="Foto de Bruno Bragança"><br>
        <strong>Bruno Bragança</strong>
      </a>
      <br>
      <a href="https://github.com/BrunoBReis">github.com/BrunoBReis</a>
    </td>
    <td></td>
    <td></td>
  </tr>
</table>

## Equipe GCES (26.2) - Em atividade

<table> <tr> 

<td align="center">
  <a href="https://github.com/luluaroeira">
    <img src="https://github.com/luluaroeira.png?size=160" width="120" alt="Foto de Ana Luiza Komatsu Aroeira"><br>
    <strong>Ana Luiza Komatsu</strong>
  </a>
  <br>
  <a href="https://github.com/luluaroeira">github.com/luluaroeira</a>
</td>

<td align="center">
  <a href="https://github.com/Ana-Luiza-SC">
    <img src="https://github.com/Ana-Luiza-SC.png?size=160" width="120" alt="Foto de Ana Luiza Soares de Carvalho"><br>
    <strong>Ana Luiza Soares</strong>
  </a>
  <br>
  <a href="https://github.com/Ana-Luiza-SC">github.com/Ana-Luiza-SC</a>
</td>

<td align="center"> <a href="https://github.com/BrunoBReis"> <img src="https://github.com/BrunoBReis.png?size=160" width="120" alt="Foto de Bruno Bragança"><br> <strong>Bruno Bragança</strong> </a> <br> <a href="https://github.com/BrunoBReis">github.com/BrunoBReis</a> </td>

</tr>

<tr> 

<td align="center">
  <a href="https://github.com/DiceRunner714">
    <img src="https://github.com/DiceRunner714.png?size=160" width="120" alt="Foto de Eduardo Matheus dos Santos Sandes"><br>
    <strong>Eduardo Matheus</strong>
  </a>
  <br>
  <a href="https://github.com/DiceRunner714">github.com/DiceRunner714</a>
</td>

<td align="center">
  <a href="https://github.com/SAnjos3">
    <img src="https://github.com/SAnjos3.png?size=160" width="120" alt="Foto de Gabriel Soares dos Anjos"><br>
    <strong>Gabriel Soares</strong>
  </a>
  <br>
  <a href="https://github.com/SAnjos3">github.com/SAnjos3</a>
</td>

<td align="center"> <a href="https://github.com/leohssjr"> <img src="https://github.com/leohssjr.png?size=160" width="120" alt="Foto de Leonardo Henrique Sobral Sauma Junior"><br> <strong>Leonardo Henrique</strong> </a> <br> <a href="https://github.com/leohssjr">github.com/leohssjr</a> </td>

</tr>

<tr> 

<td align="center">
  <a href="https://github.com/DeM4rcio">
    <img src="https://github.com/DeM4rcio.png?size=160" width="120" alt="Foto de Márcio Henrique"><br>
    <strong>Márcio Henrique</strong>
  </a>
  <br>
  <a href="https://github.com/DeM4rcio">github.com/DeM4rcio</a>
</td>

<td align="center">
  <a href="https://github.com/MVConsorte">
    <img src="https://github.com/MVConsorte.png?size=160" width="120" alt="Foto de Mateus Villela"><br>
    <strong>Mateus Villela</strong>
  </a>
  <br>
  <a href="https://github.com/MVConsorte">github.com/MVConsorte</a>
</td>

<td align="center"> <a href="https://github.com/redjsun"> <img src="https://github.com/redjsun.png?size=160" width="120" alt="Foto de Yzabella Miranda Pimenta"><br> <strong>Yzabella Miranda</strong> </a> <br> <a href="https://github.com/redjsun">github.com/redjsun</a> </td>

</tr> </table>

## Tecnologias utilizadas

- [MkDocs](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

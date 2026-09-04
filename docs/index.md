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

O fluxo oficial do projeto é via Docker: não é preciso instalar Python ou
MkDocs na máquina, nem criar ambiente virtual.

1. Suba a documentação:

```bash
make serve
```

1. Acesse a documentação:

```text
http://localhost:8000
```

1. Para encerrar:

```bash
make stop
```

Como o projeto é montado como volume no container, alterações em `docs/` e
`mkdocs.yml` são refletidas no navegador com hot reload. Se mudar o
`requirements.txt`, rode `make serve` novamente para reconstruir a imagem.

## Controle de qualidade

Antes de abrir um Pull Request, rode os checks que também são executados no CI:

```bash
make quality
```

| Comando | O que faz |
| --- | --- |
| `make lint-md` | Valida estilo e consistência do Markdown com o `markdownlint-cli2` |
| `make lint-md-fix` | Corrige automaticamente o que for corrigível |
| `make check-links` | Roda `mkdocs build --strict` e varre o HTML gerado com o `LinkChecker` |
| `make check-links-extern` | Igual ao anterior, incluindo links externos |

## Passo a passo recomendado

1. Entre na pasta do projeto.
2. Rode `make serve`.
3. Abra `http://localhost:8000`.
4. Edite os arquivos em `docs/`.
5. Veja o hot reload no navegador.
6. Rode `make quality` antes de abrir o PR.
7. Ao terminar, rode `make stop`.

## Estrutura do repositório

```text
.
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

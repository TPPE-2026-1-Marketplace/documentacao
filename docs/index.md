# DK Fashion - Documentação

Repositório da documentação do projeto **DK Fashion**.

## Sobre a documentação

Esta documentação centraliza os principais artefatos da primeira entrega do projeto, incluindo:

- backlog do produto;
- requisitos não funcionais;
- arquitetura do projeto;
- modelagem do banco de dados;
- conteinerização do ambiente

## Como executar localmente

1. Instale as dependências:

```bash
make install
```

2. Inicie o servidor local do MkDocs:

```bash
mkdocs serve
```

3. Acesse:

```text
http://127.0.0.1:8000
```

## Como executar com Docker

1. Construa a imagem e suba o container:

```bash
docker compose up --build
```

2. Acesse a documentação:

```text
http://localhost:8000
```

3. Para encerrar:

```bash
docker compose down
```

## Comparando os dois fluxos

### Fluxo com ambiente virtual

- cria uma `.venv` local;
- instala os pacotes diretamente no seu sistema;
- executa `mkdocs serve` a partir do ambiente Python do projeto.

### Fluxo com Docker

- cria uma imagem isolada com Python e MkDocs;
- sobe um container com a porta `8000`;
- monta o projeto como volume, então alterações em `docs/` e `mkdocs.yml` continuam refletindo no navegador.

## Passo a passo recomendado

1. Entre na pasta do projeto.
2. Rode `docker compose up --build`.
3. Abra `http://localhost:8000`.
4. Edite os arquivos em `docs/`.
5. Veja o hot reload no navegador.
6. Ao terminar, rode `docker compose down`.

Se mudar o `requirements.txt`, reconstrua a imagem com `docker compose up --build`.

## Estrutura do repositório

```text
.
|-- docs/
|   |-- index.md
|   |-- contributing_guidelines.md
|   |-- user_history.md
|   |-- non_functional_requirements.md
|   `-- user_history/
|-- mkdocs.yml
|-- Dockerfile
|-- compose.yaml
|-- requirements.txt
`-- README.md
```

## Equipe

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

## Tecnologias utilizadas

- [MkDocs](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

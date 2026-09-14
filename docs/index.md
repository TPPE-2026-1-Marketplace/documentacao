# DK Fashion - Documentação

Portal de documentação do **DK Fashion**, marketplace de moda desenvolvido para
uma cliente real a partir de elicitação contínua de requisitos.

## Sobre o projeto

O DK Fashion nasce da necessidade de levar para o digital uma loja de moda que
já opera fisicamente. Em vez de substituir a operação existente, a plataforma
integra os dois canais: o mesmo catálogo, o mesmo estoque e a mesma base de
clientes atendem tanto a venda presencial quanto a venda on-line.

O sistema é composto por uma loja virtual voltada ao cliente final e por um
painel administrativo usado pela equipe da loja. Entre as capacidades previstas
no [backlog](backlog.md) e nos
[requisitos não funcionais](non_functional_requirements.md) estão:

- **Catálogo e vitrine** — cadastro de produtos com variações de cor e tamanho,
  imagens, busca com filtros e página de detalhes;
- **Compra on-line** — carrinho, múltiplas formas de pagamento (Pix, crédito e
  débito), cálculo de frete, rastreamento e retirada na loja física;
- **Operação da loja** — registro de vendas presenciais, sincronização de
  estoque entre os canais, histórico auditável de alterações e níveis de acesso
  por perfil (cliente, caixa, vendedor, gerente e administrador);
- **Relacionamento e marketing** — cadastro de clientes, cupons de desconto,
  cupons de parceiros e exportação da base para campanhas de mídia paga;
- **Gestão de desempenho** — vínculo de vendedor por transação, cálculo de
  comissão, metas mensais, ranking e acompanhamento de progresso;
- **Pós-venda e fiscal** — avaliações de produtos com moderação, trocas e
  integração com emissão de NF-e.

## Objetivo desta documentação

Esta documentação organiza, em um único lugar, as fontes de conhecimento que o
projeto acumulou — decisões de produto, decisões técnicas e o registro do que
vem sendo construído:

| Fonte de conhecimento | Onde está |
| --- | --- |
| Decisões de requisitos elicitadas com a cliente: histórias de usuário e requisitos não funcionais | [Backlog](backlog.md) e [Requisitos Não Funcionais](non_functional_requirements.md) |
| Registro das conversas que originaram essas decisões | [Atas de reunião](atas_reuniao/ata_26_08_2026.md) |
| Detalhamento da arquitetura do banco de dados | [Modelo Físico do Banco de Dados](physical_data_model.md) |
| Detalhamento da prototipação e dos fluxos de interface | [Protótipo](prototipo.md) |
| Documentação das sprints e do desenvolvimento em andamento | [Sprints](sprints.md) |
| Guia de contribuição para o projeto open source | [Guia de Contribuição](contributing_guidelines.md) |
| Fluxo de branches, revisão e release adotado | [Gitflow do Projeto](gitflow.md) |

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

## Estrutura do repositório

```text
.
|-- docs/
|   |-- index.md
|   |-- backlog.md
|   |-- non_functional_requirements.md
|   |-- physical_data_model.md
|   |-- prototipo.md
|   |-- contributing_guidelines.md
|   |-- gitflow.md
|   |-- sprints.md
|   |-- atas_reuniao/
|   |-- sprints/
|   `-- user_history/
|-- slides/
|   `-- template.md
|-- qa-analytics/
|   |-- dashboard.py
|   `-- requirements.txt
|-- scripts/
|   |-- build-slides.sh
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

## Como executar

O fluxo oficial do projeto é via Docker: não é preciso instalar Python ou
MkDocs na máquina, nem criar ambiente virtual.

1. Suba a documentação:

```bash
make serve

# ou

make serve-background # sobe como Daemon
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

## Tecnologias utilizadas

As tecnologias abaixo são as do **projeto DK Fashion como um todo**, e não
apenas as deste repositório de documentação.

### Front-end

| Tecnologia | Papel |
| --- | --- |
| [React](https://react.dev/) + [TypeScript](https://www.typescriptlang.org/) | Interface da loja e do painel administrativo (SPA) |
| [Vite](https://vite.dev/) | Build e servidor de desenvolvimento |
| [TailwindCSS](https://tailwindcss.com/) | Estilização e design system da interface |
| [Figma](https://www.figma.com/) | Prototipação de alta fidelidade que guia a implementação |

### Back-end

| Tecnologia | Papel |
| --- | --- |
| [NestJS](https://nestjs.com/) + [TypeScript](https://www.typescriptlang.org/) | API REST modular, organizada por domínio |
| [TypeORM](https://typeorm.io/) | Mapeamento objeto-relacional e migrações de esquema |
| [PostgreSQL](https://www.postgresql.org/) | Banco de dados relacional |
| [JWT](https://jwt.io/) | Autenticação e controle de acesso por perfil |
| [Jest](https://jestjs.io/) | Testes automatizados |

### Documentação

| Tecnologia | Papel |
| --- | --- |
| [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) | Geração e tema do portal de documentação |
| [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) | Padronização do Markdown |
| [LinkChecker](https://linkchecker.github.io/linkchecker/) | Verificação de links quebrados |
| [Marp](https://marp.app/) | Slides das apresentações de sprint |

### Infraestrutura e qualidade

| Tecnologia | Papel |
| --- | --- |
| [Docker](https://www.docker.com/) e Docker Compose | Conteinerização dos ambientes de desenvolvimento |
| [GitHub Actions](https://docs.github.com/actions) | Integração e entrega contínuas |
| [SonarCloud](https://sonarcloud.io/) | Análise estática e métricas de qualidade do código |
| [Render](https://render.com/) e [Vercel](https://vercel.com/) | Hospedagem da API e do front-end (ver [orçamento](orcamento_hospedagem.md)) |

## Histórico de Versionamento

| Versão | Autor | Resumo | Data |
| --------------- | --------------- | --------------- | --------------- |
| `1.0` | [Bruno Bragança](https://github.com/BrunoBReis) | Criação da página inicial da documentação | 26/03/2026 |
| `1.1` | [Bruno Bragança](https://github.com/BrunoBReis) | Atualização da página inicial com a equipe do projeto | 30/03/2026 |
| `1.2` | [Bruno Bragança](https://github.com/BrunoBReis) | Atualização das instruções de execução para o fluxo com Docker | 06/04/2026 |
| `1.3` | [Bruno Bragança](https://github.com/BrunoBReis) | Inclusão da seção de controle de qualidade da documentação | 01/09/2026 |
| `1.4` | [Eduardo Matheus](https://github.com/DiceRunner714) | Adição da equipe GCES (26.2) e do atalho para servir a documentação em segundo plano | 04/09/2026 |
| `1.5` | [Bruno Bragança](https://github.com/BrunoBReis) | Descrição do projeto, objetivo da documentação e tecnologias separadas por front-end, back-end e documentação | 14/09/2026 |

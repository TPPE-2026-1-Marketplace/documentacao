#!/usr/bin/env sh
#
# Gera as apresentações de sprint com o marp-cli, em container.
#
# Uso:
#   ./scripts/build-slides.sh                  # HTML de todos os decks
#   ./scripts/build-slides.sh --pdf            # HTML + PDF de todos os decks
#   ./scripts/build-slides.sh --pptx           # HTML + PPTX de todos os decks
#   ./scripts/build-slides.sh slides/01.md     # apenas um deck
#   ./scripts/build-slides.sh --pdf slides/01.md
#
# Diferente do check-links.sh, este script roda no HOST e orquestra o
# container: a imagem do Marp é de terceiros e usa a variável MARP_USER para
# gravar os arquivos com o dono correto, então não sobrescrevemos o entrypoint
# dela.
#
set -eu

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SLIDES_DIR="$ROOT_DIR/slides"
OUT_DIR="$SLIDES_DIR/dist"

formats=""
decks=""

for arg in "$@"; do
    case "$arg" in
        --pdf)  formats="$formats --pdf" ;;
        --pptx) formats="$formats --pptx" ;;
        --*)
            echo "Opção desconhecida: $arg" >&2
            echo "Use --pdf ou --pptx." >&2
            exit 1
            ;;
        *)
            if [ ! -f "$arg" ]; then
                echo "Arquivo não encontrado: $arg" >&2
                exit 1
            fi
            decks="$decks $arg"
            ;;
    esac
done

# Sem deck explícito, gera todos os arquivos de slides/ (menos o dist/).
if [ -z "$decks" ]; then
    decks="$(find "$SLIDES_DIR" -maxdepth 1 -name '*.md' | sort | tr '\n' ' ')"
fi

if [ -z "$(printf '%s' "$decks" | tr -d ' ')" ]; then
    echo "Nenhum deck encontrado em $SLIDES_DIR" >&2
    exit 1
fi

mkdir -p "$OUT_DIR"

# A imagem grava os arquivos como este usuário; sem isso a saída sai como root.
MARP_USER="$(id -u):$(id -g)"
export MARP_USER

for deck in $decks; do
    # Caminhos precisam ser relativos à raiz do projeto, que é o diretório
    # montado no container.
    rel_deck="${deck#"$ROOT_DIR"/}"
    name="$(basename "$deck" .md)"

    echo "==> $rel_deck"

    # O HTML é sempre gerado; PDF e PPTX exigem uma execução própria, porque
    # cada uma escreve um arquivo de saída diferente.
    docker compose run --rm slides \
        "$rel_deck" --output "slides/dist/${name}.html"

    case "$formats" in
        *--pdf*)
            docker compose run --rm slides \
                "$rel_deck" --pdf --output "slides/dist/${name}.pdf"
            ;;
    esac

    case "$formats" in
        *--pptx*)
            docker compose run --rm slides \
                "$rel_deck" --pptx --output "slides/dist/${name}.pptx"
            ;;
    esac
done

echo
echo "Slides gerados em ${OUT_DIR#"$ROOT_DIR"/}/"

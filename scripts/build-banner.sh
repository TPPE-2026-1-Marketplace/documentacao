#!/usr/bin/env sh
#
# Gera o PDF de impressão do banner acadêmico (banner/banner.html).
#
# Uso (normalmente via `make banner`, que roda este script no container):
#   ./scripts/build-banner.sh
#
# Saída em banner/dist/ (não versionada):
#   banner-rgb.pdf      PDF direto do Chromium (RGB, vetorial)
#   banner-cmyk.pdf     convertido para CMYK pelo Ghostscript: envie este à gráfica
#   banner-preview.png  prévia em baixa resolução, para conferir o layout
#
# Dependências: Chromium (ou Google Chrome) e Ghostscript. A imagem do estágio
# `banner` do Dockerfile já traz os dois; no host, use CHROME=/caminho/do/binário
# se o navegador não estiver no PATH.
#
set -eu

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT_DIR/banner/banner.html"
OUT_DIR="$ROOT_DIR/banner/dist"

if [ -z "${CHROME:-}" ]; then
    for candidate in chromium chromium-browser google-chrome-stable google-chrome; do
        if command -v "$candidate" >/dev/null 2>&1; then
            CHROME="$candidate"
            break
        fi
    done
fi

if [ -z "${CHROME:-}" ]; then
    echo "Chromium/Chrome não encontrado. Rode via 'make banner' ou defina CHROME." >&2
    exit 1
fi

if ! command -v gs >/dev/null 2>&1; then
    echo "Ghostscript (gs) não encontrado. Rode via 'make banner'." >&2
    exit 1
fi

mkdir -p "$OUT_DIR"

# O Chromium precisa de um HOME gravável; no container o usuário do host
# não tem diretório próprio.
CHROME_HOME="$(mktemp -d)"
trap 'rm -rf "$CHROME_HOME"' EXIT

echo "==> HTML -> PDF (RGB)"
# O tamanho da página vem do @page do HTML (82 x 122 cm, com sangria).
# O virtual-time-budget dá tempo para fontes e imagens carregarem.
HOME="$CHROME_HOME" "$CHROME" \
    --headless=new \
    --no-sandbox \
    --disable-gpu \
    --hide-scrollbars \
    --no-pdf-header-footer \
    --virtual-time-budget=10000 \
    --user-data-dir="$CHROME_HOME/profile" \
    --print-to-pdf="$OUT_DIR/banner-rgb.pdf" \
    "file://$SRC" 2>/dev/null

echo "==> RGB -> CMYK"
# /prepress mantém as imagens em alta resolução; a conversão de cor usa os
# perfis padrão do Ghostscript. O preto do layout vira um preto composto
# (CMY + K), que fica mais profundo na lona do que o K puro.
gs -q -dSAFER -dBATCH -dNOPAUSE \
    -sDEVICE=pdfwrite \
    -dPDFSETTINGS=/prepress \
    -dAutoRotatePages=/None \
    -sColorConversionStrategy=CMYK \
    -sProcessColorModel=DeviceCMYK \
    -o "$OUT_DIR/banner-cmyk.pdf" \
    "$OUT_DIR/banner-rgb.pdf"

echo "==> Prévia PNG"
gs -q -dSAFER -dBATCH -dNOPAUSE \
    -sDEVICE=png16m -r20 \
    -dTextAlphaBits=4 -dGraphicsAlphaBits=4 \
    -o "$OUT_DIR/banner-preview.png" \
    "$OUT_DIR/banner-cmyk.pdf"

pages="$(gs -q -dNODISPLAY -dNOSAFER -c "($OUT_DIR/banner-cmyk.pdf) (r) file runpdfbegin pdfpagecount = quit" 2>/dev/null || echo '?')"
if [ "$pages" != "1" ]; then
    echo "Atenção: o PDF tem $pages página(s); o esperado é 1. Algum bloco passou do tamanho do banner." >&2
fi

echo
echo "Banner gerado em ${OUT_DIR#"$ROOT_DIR"/}/ (envie o banner-cmyk.pdf para a gráfica)"

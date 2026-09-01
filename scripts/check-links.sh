#!/usr/bin/env sh
#
# Verifica links quebrados na documentação.
#
# Uso:
#   ./scripts/check-links.sh            # apenas links internos (padrão do CI)
#   ./scripts/check-links.sh --extern   # inclui links externos (rede)
#
set -eu

SITE_DIR=/tmp/site-check
PORT=8123
URL="http://127.0.0.1:${PORT}/"
LINKCHECKERRC="$(dirname "$0")/../.linkcheckerrc"

# --strict transforma avisos do MkDocs (links internos e itens de nav
# quebrados, por exemplo) em erro.
mkdocs build --strict --site-dir "$SITE_DIR"

# O site precisa ser servido por HTTP: os caminhos absolutos gerados pelo tema
# (ex.: /documentacao/...) não resolvem sobre file://, o que geraria dezenas de
# falsos positivos.
python -m http.server "$PORT" --bind 127.0.0.1 --directory "$SITE_DIR" >/dev/null 2>&1 &
server_pid=$!
trap 'kill "$server_pid" 2>/dev/null || true' EXIT

# Aguarda o servidor aceitar conexões antes de começar a checagem.
attempt=0
until python -c "import urllib.request; urllib.request.urlopen('${URL}')" 2>/dev/null; do
    attempt=$((attempt + 1))
    if [ "$attempt" -ge 30 ]; then
        echo "Servidor local não respondeu em ${URL}" >&2
        exit 1
    fi
    sleep 0.5
done

if [ "${1:-}" = "--extern" ]; then
    # Links externos ficam fora do check padrão porque dependem de rede e de
    # sites de terceiros. Ignoramos o servidor de desenvolvimento citado nos
    # docs (porta 8000 - a porta 8123 é a deste script e PRECISA ser varrida)
    # e o próprio domínio publicado (o tema gera links absolutos para ele, que
    # não existem no site servido localmente).
    linkchecker -f "$LINKCHECKERRC" --no-robots --check-extern \
        --ignore-url '^https?://(127\.0\.0\.1|localhost):8000' \
        --ignore-url '^https?://.*github\.io/documentacao' \
        "$URL"
else
    linkchecker -f "$LINKCHECKERRC" --no-robots "$URL"
fi

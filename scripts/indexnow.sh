#!/usr/bin/env bash
# Submit every URL in sitemap.xml to IndexNow.
#
# Run this after the key file is live at:
#   https://crrelabs.com/855385d2516e45a3be59c8aacd9c5dc4.txt
# IndexNow checks that URL before accepting the list. The key is public.
#
#   bash scripts/indexnow.sh
#
# Requires curl and python3. Prints the HTTP status and response body.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SITEMAP="${ROOT}/sitemap.xml"
KEY="855385d2516e45a3be59c8aacd9c5dc4"
HOST="crrelabs.com"
KEY_LOCATION="https://${HOST}/${KEY}.txt"
BODY="$(mktemp)"
trap 'rm -f "$BODY"' EXIT

python3 - "$SITEMAP" "$HOST" "$KEY" "$KEY_LOCATION" "$BODY" << 'PY'
import json
import sys
import xml.etree.ElementTree as ET

sitemap, host, key, key_location, dest = sys.argv[1:]
ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
locs = []
for loc in ET.parse(sitemap).findall(".//sm:loc", ns):
    if loc.text and loc.text.strip():
        locs.append(loc.text.strip())
if not locs:
    sys.exit("sitemap.xml has no <loc> entries")
payload = {
    "host": host,
    "key": key,
    "keyLocation": key_location,
    "urlList": locs,
}
with open(dest, "w", encoding="utf-8") as handle:
    json.dump(payload, handle, ensure_ascii=False)
print(f"Submitting {len(locs)} URLs from {sitemap}", file=sys.stderr)
PY

curl --fail-with-body -sS -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json; charset=utf-8" \
  --data-binary @"$BODY"
echo

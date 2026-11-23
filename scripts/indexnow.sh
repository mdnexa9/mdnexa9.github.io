#!/usr/bin/env bash
# يرسل كل روابط الـ sitemap إلى IndexNow (Bing, Yandex, Naver, Seznam, Yep).
# يعمل تلقائياً من GitHub Actions عند كل تحديث للموقع، ويمكن تشغيله يدوياً:
#   HOST=mdnexa9.github.io INDEXNOW_KEY=xxxxxxxx SITEMAP=sitemap.xml ./scripts/indexnow.sh
set -euo pipefail

: "${HOST:?HOST مطلوب}"
: "${INDEXNOW_KEY:?INDEXNOW_KEY مطلوب}"
SITEMAP="${SITEMAP:-sitemap.xml}"
KEY_LOCATION="${KEY_LOCATION:-https://$HOST/$INDEXNOW_KEY.txt}"
DRY_RUN="${DRY_RUN:-0}"

[ -f "$SITEMAP" ] || { echo "::error::لم أجد $SITEMAP"; exit 1; }

mapfile -t URLS < <(grep -oE '<loc>[^<]+</loc>' "$SITEMAP" | sed -E 's#</?loc>##g' | tr -d ' \r')
if [ "${#URLS[@]}" -eq 0 ]; then
  echo "::error::لا توجد روابط في $SITEMAP"; exit 1
fi
echo "عدد الروابط في $SITEMAP: ${#URLS[@]}"

# انتظر انتهاء نشر الموقع (GitHub Pages) قبل الإشعار — بحد أقصى نحو 5 دقائق.
ready=0
for i in $(seq 1 20); do
  code=$(curl -s -o /dev/null -m 20 -w '%{http_code}' -L "https://$HOST/" || echo 000)
  if [ "$code" = "200" ]; then ready=1; break; fi
  echo "الموقع يرد $code — انتظار النشر ($i/20)"
  sleep 15
done
[ "$ready" = "1" ] || echo "::warning::الموقع لم يرد 200 بعد الانتظار؛ سأرسل الروابط على أي حال"

printf '%s\n' "${URLS[@]}" > urls.txt
jq -Rs --arg host "$HOST" --arg key "$INDEXNOW_KEY" --arg keyLocation "$KEY_LOCATION" \
  '{host:$host, key:$key, keyLocation:$keyLocation,
    urlList:(split("\n") | map(gsub("^\\s+|\\s+$";"")) | map(select(length>0)))}' \
  urls.txt > indexnow-payload.json

if [ "$DRY_RUN" = "1" ]; then
  echo "DRY_RUN — الحمولة التي كانت ستُرسل:"
  cat indexnow-payload.json
  exit 0
fi

ok=0
for endpoint in https://api.indexnow.org/indexnow https://www.bing.com/indexnow https://yandex.com/indexnow; do
  code=$(curl -s -m 30 -o /dev/null -w '%{http_code}' -X POST "$endpoint" \
    -H 'Content-Type: application/json; charset=utf-8' --data-binary @indexnow-payload.json || echo 000)
  echo "$endpoint -> HTTP $code"
  case "$code" in 200|202) ok=1 ;; esac
done

if [ "$ok" = "1" ]; then
  echo "تم إرسال ${#URLS[@]} صفحة إلى محركات البحث."
else
  echo "::error::فشل الإرسال إلى كل المحركات."; exit 1
fi

#!/bin/bash

# 登録に使うデータ
IMAGE_URL="http://example.com/sample.jpg"
MODEL_NAME="example_model"
PROMPT="a test prompt"
NEGATIVE_PROMPT="bad image"

# == INSERT ==
echo "== Insert ImagePrompt =="
curl -s -X POST "http://localhost:8000/insert_ImagePrompt/" \
  --get \
  --data-urlencode "image_url=${IMAGE_URL}" \
  --data-urlencode "model_name=${MODEL_NAME}" \
  --data-urlencode "prompt=${PROMPT}" \
  --data-urlencode "negative_prompt=${NEGATIVE_PROMPT}"
echo ""

# == GET ==
echo "== Get ImagePrompts =="
RESPONSE=$(curl -s "http://localhost:8000/get_ImagePrompt/")
echo "$RESPONSE" | jq
echo ""

# 最後のIDを抽出
LAST_ID=$(echo "$RESPONSE" | jq '.[-1].id')

# == DELETE ==
echo "== Delete ImagePrompt ID=$LAST_ID =="
curl -s -X DELETE "http://localhost:8000/delete_ImagePrompt/?id=${LAST_ID}"
echo ""

# == Final GET ==
echo "== Final Get ImagePrompts =="
curl -s "http://localhost:8000/get_ImagePrompt/" | jq
echo ""

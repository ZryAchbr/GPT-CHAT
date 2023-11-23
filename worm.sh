#!/bin/sh

if [ -z "$1" ]; then
  echo "Usage: $0 <input_text>"
  exit 1
fi

input_text="$1"

echo "\n[+] Input: $input_text"
echo "\n[+] Output:" 

curl_output=$(curl -s https://api.openai.com/v1/completions \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $CHATGPT_TOKEN" \
  -d '{
  "model": "text-davinci-003",
  "prompt": "'"$input_text"'",
  "max_tokens": 4000,
  "temperature": 1.0
}' \
--insecure | jq -r '.choices[].text')

echo "$curl_output"

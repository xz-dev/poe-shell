#!/usr/bin/env sh

set -e

bot_name=$1
chat_content=$2

bot_in_name=$(./helper/poe-botname.sh $bot_name)

echo "Get the search key from "$bot_in_name
search_key_word=$(./poe-shell.py send_message $bot_in_name '(you should only tell me the search text) please tell me the search key of "'$chat_content'"'  | jq -r '.text_new' | tr -d '\n')

echo "Search the key word "$search_key_word
searched_content=$(curl --data-urlencode "q="$search_key_word'"' https://searx.work/search)
echo "Ask your question again with the searched content to "$bot_in_name
./poe-shell.py send_message $bot_in_name $chat_content"\nUnder is searched from search engine\n$searched_content"

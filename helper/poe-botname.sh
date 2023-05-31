#!/usr/bin/env sh

./poe-shell.py bot_names | jq -r --arg value "$1" '. | to_entries[] | select(.value == $value) | .key'

#!/bin/bash

operate="$1"
key="$2"
authorized_keys_file="$3"

if [ -z "$operate" ] || [ -z "$key" ] || [ -z "$authorized_keys_file" ]; then
  echo "Usage: bash add_remove_public_key_in_authorized_keys.sh <operate> <key> <authorized_keys_file>"
  exit 1
fi
if [ ! -f "$authorized_keys_file" ]; then
  echo "File $authorized_keys_file does not exist"
  exit 1
fi

if [ "$operate" = "add" ]; then
  if grep -qF "$key" "$authorized_keys_file"; then
    echo "Public key already exists in $authorized_keys_file file"
  else
    echo "$key" >>"$authorized_keys_file"
    echo "Public key added to $authorized_keys_file file"
  fi
elif [ "$operate" = "remove" ]; then
  if grep -qF "$key" "$authorized_keys_file"; then
    sed -i -e "\|$key|d" "$authorized_keys_file"
    echo "Public key removed from $authorized_keys_file file"
  else
    echo "Public key does not exist in $authorized_keys_file file"
  fi
else
  echo "Invalid operate: $operate. Supported operates are 'add' and 'remove'"
  exit 1
fi

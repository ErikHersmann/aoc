#!/bin/bash

FILE="main.py"
LAST_HASH=""

# Ensure the file exists
if [[ ! -f "$FILE" ]]; then
  echo "File $FILE does not exist."
  exit 1
fi

while true; do
  # Wait for the file to close after being modified
  inotifywait -e close_write "$FILE"

  # Calculate the current hash of the file
  CURRENT_HASH=$(md5sum "$FILE" | awk '{ print $1 }')

  # Compare the current hash with the last hash
  if [[ "$CURRENT_HASH" != "$LAST_HASH" ]]; then
    # Update the last hash
    LAST_HASH=$CURRENT_HASH

    # Clear the terminal and run the script
    clear && python3 "$FILE"
  fi
done

#!/bin/bash
set -e
TEMP_FOLDER=""
EDITOR=""

s3uri="$1"
filename=$(echo "$s3uri" | awk -F "/" '{print $NF}')

aws s3 cp s3uri "$TEMP_FOLDER"
cp "$TEMP_FOLDER/$filename" "$TEMP_FOLDER/${filename}.bak"
"$EDITOR" "$TEMP_FOLDER/${filename}.bak" "$TEMP_FOLDER/$filename"
echo -n "Upload changes? y/n: "
read -r choice
if [[ "$choice" == "y" ]];then
  aws s3 cp "$TEMP_FOLDER/$filename" s3uri
fi

#!/bin/bash

echo "Enter Directory or File Path"
read -r path

if [ ! -e "$path" ]; then
    echo "File or directory does not exist."
    exit 1
fi

echo "Menu:"
echo "1. Short file description"
echo "2. Long file description"
echo "3. Hidden files"
echo "Enter your choice"
read -r choice

case "$choice" in
    1) echo "Short file description:"
       ls -1 "$path";;
    2) echo "Long file description:"
       ls -l "$path";;
    3) echo "Hidden files:"
       ls -a "$path";;
    *) echo "Invalid choice";;
esac

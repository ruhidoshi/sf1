#!/bin/bash
echo "enter the filename: "
read filename

words=$(wc -w < "$filename")
characters=$(wc -c < "$filename")
lines=$(wc -l < "$filename")

echo "Words: $words"
echo "Characters: $characters"
echo "Lines: $lines"

#!/bin/bash
echo "Enter a number: "
read num
reversed=0
while [ "$num" -ne 0 ]; do
  remainder=$((num % 10))
  reversed=$((reversed * 10 + remainder))
  num=$((num / 10))
done
echo "Reversed number: $reversed"

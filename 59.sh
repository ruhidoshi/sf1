#!/bin/bash
echo "Enter a number: "
read num
sum=0
while [ "$num" -ne 0 ]; do
  remainder=$((num % 10))
  sum=$((sum + remainder))
  num=$((num / 10))
done
echo "Sum of individual digits: $sum"

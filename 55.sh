#!/bin/bash

echo "Enter the number of terms: "
read n

a=0
b=1

echo "Fibonacci series:"
for ((i = 0; i < n; i++)); 
do
  echo -n "$a "
  next=$(a + b)
  a=$b
  b=$next
done
echo

#!/bin/bash
echo Enter a number
read a
let fact=1

for((i=1;i<=$a;i++))
do
let fact=fact\*i
echo $fact
done

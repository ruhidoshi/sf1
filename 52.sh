#!/bin/bash
echo Enter Directory Name
read d
echo menu
echo 1. Short file description 
echo 2. Long file description 
echo 3. Hidden files
echo Enter your choice
read a
case $a in
1) ls $d
;;
2) ls -l $d
;;
3) ls -d $d
;;
*) echo invalid choice
;;
esac

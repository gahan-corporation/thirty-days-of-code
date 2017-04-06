#!/usr/bin/bash

# Apparently there's no HackerRank test for this so I'll just write the code here.

read -t 1 int
read -t 1 dec
read -t 1 str

if [[ $? -ne 0 ]]
then
  export int=8
  export dec=12
  export str="Run's house" 
else
  echo "$int + $dec" | bc -l
  echo "$dec + $dec" | bc -l
  echo "$str is the best place to learn and practice coding!\n"
fi 

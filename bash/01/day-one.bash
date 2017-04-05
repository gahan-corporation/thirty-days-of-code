#!/usr/bin/bash

# Apparently there's no HackerRank test for this so I'll just write the code here.

read -t 5 int
read -t 5 dec
read -t 5 str

if [[ $? -ne 0 ]]
then
  echo "There weren't no input."
else
  echo "$int + $dec" | bc -l
  export add_dec = $dec + $dec
  export add_str = "$str is the best place to learn and practice coding!\n"

  echo $add_int
fi 

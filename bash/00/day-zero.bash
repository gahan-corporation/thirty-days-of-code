#!/usr/bin/bash

read -t 5 inputString # get a line of input from stdin and save it to our variable

# Your first line of output goes here
echo 'Hello, World.'


# Write the second line of output
if [[ $? -ne 0 ]]
then
  echo "There weren't no input."
else
  echo $inputString
fi

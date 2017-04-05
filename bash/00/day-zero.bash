#!/usr/bin/bash

read -t 5 inputString # get a line of input from stdin and save it to our variable

# Write the second line of output
if [[ $? -ne 0 ]]
then
  export inputString="There weren't no input."
fi

# Your first line of output goes here
echo 'Hello, World.'

echo $inputString

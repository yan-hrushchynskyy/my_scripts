#!/bin/bash

echo "Enter terraform command: "
read terraform_command
path=$(pwd)
res=$(find $path/* -type d -not -path '*/\.*') # recursively checking all directories except hidden
for i in $res
do
echo "========== working with $i directory =========="
cd $i
file1=($i/*.tf) # looking for .tf files
if [ -f "$file1" ]; then
echo "yes" | $terraform_command
cd $path
else
echo "there are no tf files in `pwd`"
fi
done
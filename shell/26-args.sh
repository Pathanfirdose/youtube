#!/bin/bash
set -x
#to acces all args
if [ $# -eq 0 ]
then 
    echo please provide one arg
    exit 1
fi

echo "first argument passed is $1"
echo "second arument passed is $2"

echo all arguments passed is $@
echo number of arguments passed is $#

for file in $@
do
    echo copying file $file
done


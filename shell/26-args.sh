#!/bin/bash
set -x
echo "first argument passed is $1"
echo "second arument passed is $2"

echo all arguments passed is $@
echo number of arguments passed is $#

for file in $@
do
    echo copying file $file
done


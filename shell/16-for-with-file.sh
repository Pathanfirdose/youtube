#!/bin/bash

FILENAME=/home/ec2-user/youtube/shell/names.txt

for names in $(cat $FILENAME)
do
    echo "name is $names"
done


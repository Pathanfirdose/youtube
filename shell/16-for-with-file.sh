#!/bin/bash

FILENAME=/home/ec2-user/youtube/shell/names.txt

for names in $(cat $FILENAME)
do
    echo "name is $names"
done

for ip in google.com facebook.com
do
    ping $ip
    sleep 10
done
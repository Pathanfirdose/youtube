#!/bin/bash

FU=$(df -H | egrep "Filesystem|tmpfs" | grep "sda2" | awk '{print $5}' | tr -d % )
TO="pfirdose1988@gmail.com"

if [ $FU -ge 80 ]
then
    echo disk space is full | mail -s "disk space is alert!" $TO
else
    echo all good
fi
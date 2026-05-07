#!/bin/bash

ping -c 1 www.google.com >> ping.txt

for i in www.google.com www.facebook.com
do
    ping -c 2 $i
done

#to run script on specific time only single time use command: at 11:30 AM then bash /path/ then ctrl+D now it is scheduled if you want to see then run command: atq then if you want to remove q command is atrm

'''
at 02:58 AM
    bash /path/to/script
    ctrl+D
atq # to see the que of scripts scheduled
atrm <no> # to delete script from que atrm + que no.

'''
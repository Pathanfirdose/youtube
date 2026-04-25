#!/bin/bash

ping -c 1 www.google.com >> ping.txt

for i in facebook.com, www.google.com
do
    ping -c 2 $i
done

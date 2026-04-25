#!/bin/bash

ping -c 1 www.google.com >> ping.txt

for i in www.google.com, facebook.com
do
    ping -c 2 $i
done

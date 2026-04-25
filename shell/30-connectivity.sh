#!/bin/bash

read -p "which site you want to ping ? " site

ping -c 1 $site
# sleep 1s

if [ $site -eq 0 ]
then
    echo succesfully connected to $site
else
    echo unable to connect $site
fi  
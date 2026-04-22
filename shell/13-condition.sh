#!/bin/bash

read -p "enter your age" age
read -p "enter your country" country

if [ $age -gt 40 ] && [ $country -eq "india"]
then
    echo "you can vote"
else
    echo "you cant vote"
fi
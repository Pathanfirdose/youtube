#!/bin/bash

# read -p "enter your age" age
# read -p "enter your country" country

# if [ $age -gt 40 ] && [ $country -eq "india"] # && and condition
# then
#     echo "you can vote"
# else
#     echo "you cant vote"
# fi

read -p "enter your age" age
read -p "enter your country" country

if [ $age -gt 40 ] || [ $country == "india"] # || or condition
then
    echo "you can vote"
else
    echo "you cant vote"
fi
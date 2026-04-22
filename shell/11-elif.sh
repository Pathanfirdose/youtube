#!/bin/bash

read -p "enter your marks" marks

if [ $marks -ge 80 ]
then
    echo "you are first class"
elif [ $marks -ge 60 ]
then
    echo "you are second class"
elif [ $marks -ge 40 ]
then
    echo "you are third class"
else
    echo "you are fail.......betterluck next time"
fi
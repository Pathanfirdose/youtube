#!/bin/bash

count=0
num=10

while [ $count -le $num ] # it runs until count is less than equal to num that till its true it runs once it is fales then stops
do
    echo "value of count var is $count"
    let count++ # every time it increase the value of count 0+1 0+2 0+3
done


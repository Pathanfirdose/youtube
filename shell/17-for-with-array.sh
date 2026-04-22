#!/bin/bash

myarray=(1 2 3 hello hai dhurandhar)

length=${#myarray[@]}

for ((i=0;i<$length;i++)) # c style loop separated by ; i=0 loop starts at 0 index then ; i<$length this is condition then ; i++ here it increase the index value of i for example first it is i=0 then i+0+1 then i+0+2 it runs until i index value is less than 6
do
    echo "value of array is ${myarray[$i]}"
done
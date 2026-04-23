#!/bin/bash

#example of break in loop
# we just need to confirm given number exist or not

no=6

for i in 1 2 3 4 5 6 7 8 9 10
do
    let r=$i%2
    if [ $r -eq 0 ]
    then
        continue
    fi
    echo odd number is $i
done
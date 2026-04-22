#!/bin/bash

#Array

myarray=(1 30 50 firdose "ghouse khan")

echo "this is my array value in third index ${myarray[2]}"

echo "all values in it ${myarray[@]}"

# how  to get lenght of array

echo "no of arrays in this ${#myarray[@]}"

echo "pick specific values ${myarray[@]:1:3}"

# updating array 

myarray+=(100 200 300)

echo "updated values ${myarray[@]}
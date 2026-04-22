#!/bin/bash

#Array

myarray=(1 30 50 firdose "ghouse khan")

echo "this is my array value in third index ${myarray[2]}"

echo "all values in it ${myarray[@]}"

# how  to get lenght of array

echo "no of arrays in this ${#myarray[@]}"
echo "no of arrays in this ${myarray[#@]}"
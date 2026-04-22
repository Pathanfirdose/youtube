#!/bin/bash

myvar="hey sabir how are you"

myvarlength=${#myvar}

echo "length of my vars $myvarlength"
echo "length of my vars ${#myvar}"

echo "upper case is ----- ${myvar^^}"
echo "lower case is ----- ${myvar,,}"

# to replace a string

newVar=${myvar/sabir/riyaz}
echo "my new var is $newVar"

# to slice a string
echo "after slice ${myvar:4:5}"
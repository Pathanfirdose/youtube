#!/bin/bash

declare -A myarray

myarray=([name]=firdose [age]=40 [town]=rayachoy)

echo "my details are ${myarray[name]}"
echo "my details are ${myarray[age]}"
echo "my details are ${myarray[town]}"
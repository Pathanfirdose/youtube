#!/bin/bash

while IFS="," id name age
do
    echo "id is $id"
    echo "name is $name"
    echo "age is $age"
done < details.csv

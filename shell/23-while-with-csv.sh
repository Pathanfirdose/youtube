#!/bin/bash

cat details.csv | awk 'NR!=1 {print}' | while IFS="," read id name age # this means to exclude first line
do
    echo "id is $id"
    echo "name is $name"
    echo "age is $age"
done < details.csv

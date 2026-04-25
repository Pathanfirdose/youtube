#!/bin/bash

FILPATH=/home/ec2-user/myscripts/text.csv

if [ -f $FILPATH ]
then
    echo file exists
else
    echo file doesnt exist
    exit 1
fi
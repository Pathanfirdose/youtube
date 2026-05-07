#!/bin/bash

FREE_SPACE=$(free -mt | grep "Total" | awk '{print $4}')
TH=500

if [ $FREE_SPACE -lt $TH ]
then
    echo ram is low
else
    echo ram has enough memory- $FREE_SPACE
fi

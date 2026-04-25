#!/bin/bash

if [ $UID -eq 0 ]
then
    echo user is root
else
    echo user is non root
fi
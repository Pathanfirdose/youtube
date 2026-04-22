#!/bin/bash

echo "provide an option"
echo "a for date"
echo "b for current working directory"
echo "c for list of files and directories"

read choice

case $choice
        a)date;;
        b)pwd;;
        c)ls;;
        *)echo "enter valid value"
esac
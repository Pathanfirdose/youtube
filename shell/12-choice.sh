#!/bin/bash

echo "provide an option"
echo "a for date"
echo "b for current working directory"
echo "c for list of files and directories"

read choice

case $choice in
        a)date;;
        b)pwd;;
        c)ls;;
        *)echo "enter valid value"
esac

echo "provide an option"
echo "a for date"
echo "b for current working directory"
echo "c for list of files and directories"

read choice

case $choice in
        a)      
                echo "today date is .."
                date
                echo "end..."
                ;;
        b)pwd;;
        c)ls;;
        *)echo "enter valid value"
esac
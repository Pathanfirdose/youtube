#!/bin/bash

# script should be run with sudo or root user
if [ "${UID}" -ne 0 ]
then
    echo 'please run with sudo or root'
    exit 1
fi

# provide atleast one argument
if [ "${#}" -lt 1 ]
then
    echo "usage ${0} username [comment]..."
    echo "create a user with username and comment"
    exit 1
fi

# store first argument as username
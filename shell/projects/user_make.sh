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
USER_NAME=${1}
echo $USER_NAME

# shit comment
shift
COMMENT=${@}

#CREATE PASSWORD
PASSWORD=$(date +%s%N)
echo $PASSWORD

# create the user
useradd -c "about user" -m $USER_NAME

#check user creation
if [ ${?} -ne 0 ]
then
    echo user not created
    exit 1
fi

# ste password for user
echo $PASSWORD | passwd --stdin $USER_NAME

# check password correctly set
if [ ${?} -ne 0 ]
then
    echo password not set
    exit 1
fi

# force password change on first login
passwd -e $USER_NAME

# display username,host and other
echo
echo username: $USER_NAME
echo
echo password: $PASSWORD
echo 
echo hostname is $(hostname)
#!/bin/bash

#$Revision:001$
#$Date$

#variables
BASE=/home/ec2-user/myscripts
DAYS=10
DEPTH=1
RUN=0

#CHECK IF DIRECTORY IS PRESENT OR NOT
if [ ! -d $BASE ]
then
    echo directory doesnt exists: $BASE
    exit 1
fi

#create archive folder if not present
if [ ! -d $BASE/archive ]
then
    mkdir $BASE/archive
fi

# find the list of files larger than 20 MB
for i in 'find $BASE -maxdepth $DEPTH -type f -size +20M'
do
    if [ $RUN -eq 0 ]
    then
        echo "[$(date "+%y-%m-%d %H:%M:%S")] archiving $i ==> $BASE/archive"
        gzip $i || exit 1
        mv $i.gz $BASE/archive || exit 1
    fi 
done

'''
crontab -e
    05 01 ***/home/ec2-user/myscripts/archive_project.sh
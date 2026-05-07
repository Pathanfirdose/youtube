#!/bin/bash

for i in 1 2 3 4 5 6 7 8 9
do
    echo "no. is $i"
    sleep 3s
done

for names in firdose sabir riyaz "arshad ali"
do
    echo "my friend is $names"
done

# whene ever you want to run script in background and write output to file(nohup.out) use command: nohup ./15-forloop1.sh &
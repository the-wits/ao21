#!/usr/bin/env bash

echo "Insert the number of the day:\n"
read day

if [ $day -gt 25 ]
then
    echo -e "\n[ERROR]\nEnter a number between 1 and 25"
    exit 0
fi

mkdir -p day$day
touch -a day$day/ex.txt
touch -a day$day/input.txt
cp -n template.py day$day/script.py

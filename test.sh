#!/bin/bash
echo "Enter you character"
read t

if [ $t == 'Y' ] || [ $t == 'y' ];
then
    echo "YES"
elif [ $t == 'N' ] || [ $t == 'n' ];
then
    echo "NO"
else
    echo "Invalid Input"
fi
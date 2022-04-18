#!/bin/bash
# Script to see if the variable holds value or not
var1 = " "
var2=linuxtechi
if [ -n $var1 ]
        then
                echo "string  is not empty"
        else
                echo "string provided is empty"
fi
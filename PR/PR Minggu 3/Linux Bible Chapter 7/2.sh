#!bin/bash

ONE=$1
TWO=$2
THREE=$3
X=3
Y=$(($ONE+$TWO+$THREE))

echo "There are $X parameters that include $Y."
echo "The first is $ONE, the second is $TWO, the third is $THREE."

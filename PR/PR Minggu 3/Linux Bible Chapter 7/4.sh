#!bin/bash


read -p "What is your favorite operating system? " os

if [ $os = "Windows" ] || [ $os = "Mac" ] ; then
    echo "Bad Choice!"
elif [ $os = "Linux" ] ; then
    echo "Great Choice!"
else
    echo "Is $os an operating system?"
fi

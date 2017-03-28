#!/usr/bin/python

def donuts(count):

  a=''

  if count<10:
    a=count
  else:
    a='many'

  return ('Number of donuts: ')+str(a)


print(donuts(input('How many donuts: ')))

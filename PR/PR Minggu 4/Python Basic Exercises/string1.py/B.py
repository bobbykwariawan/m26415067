#!/usr/bin/python

def both_end(s):

  a=''

  if len(s)<2:
    return a

  else:
    a=s[:2]+s[-2:]
    return a

print(both_end(raw_input('String: ')))

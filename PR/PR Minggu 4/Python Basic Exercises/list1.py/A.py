#!/usr/bin/python

def match_ends(words):

  a=words

  if len(a)>2 and a[0]==a[len(a)-1]:
    a=len(a)

  else:
    a=0

  return a

print(match_ends(raw_input('Input words: ')))

#!/usr/bin/python

def mix_up(a, b):

  c = a.replace(a[0], b[0], 1)+' '+b.replace(b[0], a[0], 1)
  return c

print(mix_up(raw_input('String 1: '), raw_input('String 2: ')))

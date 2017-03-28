#!/usr/bin/python

def fix_start(s):

  a=''
  b=''

  if len(s)>1:
    a=s.replace(s[0], '*')
    b=a.replace(a[0], s[0], 1)
    return b

print(fix_start(raw_input('String: ')))

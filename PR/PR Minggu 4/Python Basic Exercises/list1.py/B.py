#!/usr/bin/python

def front_x(words):

  a=[]
  sorted(words)
  for i in words:
    if i.startswith('x') or i.startswith('X'):
      a.append(i)
      words.remove(i)

  for i in words:
    a.append(i)


  return a

print(front_x(['mix', 'xanadu', 'asasd', 'jgijiog', 'xasdasd']))


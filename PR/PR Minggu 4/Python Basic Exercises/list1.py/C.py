#!/usr/bin/python

def sort_last(tuples):
  sorted(tuples, key=lambda s : s[-1])
  return tuples


print(sort_last([(1,7),(1,3),(3,4,5),(2,2)]))


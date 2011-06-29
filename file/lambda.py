#!/usr/bin/python

def make_repeter(n):
    return lambda s: s * n

twice = make_repeter(2)

#print twice('word')
#print twice(5)
#print make_repeter('word')
#print make_repeter(5)

#!/usr/bin/python

name = 'swaroop'
if name.startswith('swa'):
    print 'Yes, it start the strint "swa"'
if name.find('war') != -1:
    print 'Yes it contains the string "war"'
if 'a' in name:
    print 'Yes, it contains the string "a"'
delimiter = '_*_'
mylist = ['Brizil', 'Russia', 'India', 'China']
print delimiter.join(mylist)

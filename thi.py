#!/usr/bin/python

def func(x, y):
    '''Print values max of 2 nums

    The 2 nums must int'''
    x = int(x) #convert to int ,if possible
    y = int(y)
    
    if x > y:
        print x, "is the max"
    else:
        print y, "is the max"
func(3, 5)
print func.__doc__

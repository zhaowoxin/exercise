#!/usr/bin/python

class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, lenth, atleast):
        Exception.__init__(self)
        self.lenth = lenth
        self.atleast = atleast

try:
    s = raw_input('Enter something -->')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)

except EOFError:
    print '\nWhy did you do an EOF on me'
except ShortInputException, x:
    print 'ShortInputException: The input ws of lenth %d,\
    was expecting at least %d' % (x.lenth, x.atleast)
else:
    print 'No exception was raised'

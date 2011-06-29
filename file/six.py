#!/usr/bin/python

import sys

def readfile(filename):
    '''Print a file to the standard output'''
    f = file(filename)
    while True:
       line = f.readline()
       if len(line) == 0:
           break
       print line,
    f.close()

if len(sys.argv) < 2:
    print 'No action specified'
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version':
        print 'Version 1.2'
    elif option == 'help':
        print '''\
        This program prints files to STDOUT'''
    else:
        print 'Unknow option.'
        sys.exit()
else:
    for filename in sys.argv[1:]:
        print filename
        readfile(filename)
        

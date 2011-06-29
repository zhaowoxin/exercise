#!/usr/bin/python

zoo = ('wolf', 'elephent', 'penguin')
print dir(zoo)
print 'Numner of animals in the zoo is:', len(zoo) 

new_zoo = ('monkey', 'dolphin', zoo)
print 'Number of animals in the new zoo is', len(new_zoo)
print 'All anmials in new zoo are', new_zoo
print 'Animals brought from old zoo are', new_zoo[2]
print 'Last animal broutht from old zoo is', new_zoo[2][2] 

#!/usr/bin/python

ab = {  'swaroop' : 'swaroop#126.com',
        'larry'   : 'larry@wall.com',
        'Marry'   : 'marry@gmail.com',
        'smpmmae' : 'smpmmae@@163.com'
     }
print dir(ab)
print ab.__sizeof__()
ab['guido'] = 'guiduo@python.org'
del ab['smpmmae']
for name, address in ab.items():
    print 'Contact %s at %s' % (name, address)

if 'guido' in ab:
    print '\nGuiduo`s address is %s' % ab['guido']
    print 'hello'

#!/usr/bin/python

class Person:
    '''Repesent a person'''
    popular = 0

    def __init__(self, name):
        '''Init the person`s data'''
        self.name = name
        print 'Init %s' % self.name
        Person.popular += 1

    def __del__(self):
        '''I am dying'''
        print '%s says bye' % self.name
        Person.popular -= 1

        if Person.popular == 0:
            print 'I am the last one'
        else:
            print 'There are %d people left' %Person.popular
    def sayhi(self):
        '''Greeting by the person
        Really, that`s all it does'''
        print 'Hi, my name is %s' % self.name
    def howmany(self):
        '''Prints the current population'''
        print 'I am %d persons here' % Person.popular
p = Person('zhaoyang')
p.sayhi()
p.howmany()

q = Person('dongkai')
q.sayhi()
q.howmany()

p.sayhi()
p.howmany()

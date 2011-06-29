#!/usr/bin/python

class SchoolMember:
    '''Represent any school members'''
    def __init__(self, name, age):
        self.age = age
        self.name = name
        print '(Int SchoolMember is %s)' % self.name
    def tell(self):
        '''Tell my details'''
        print 'Name is %s, Age is %s.' % (self.name, self.age)
class Teacher(SchoolMember):
    '''Represents a tercher'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
    def tell(self):
        SchoolMember.tell(self)
        print 'Salary is %d' % self.salary

class Student(SchoolMember):
    '''Represents a student'''
    def __init__(self, name, age, mark):
        SchoolMember.__init__(self, name, age)
        self.mark = mark
    def tell(self):
        SchoolMember.tell(self)
        print 'Mark is %d' % self.mark

t = Teacher('Mrs, Shrividya', 40, 30000)
s = Student('zhaoyang', 22, 100)

print 

members = [t, s]
for member in members:
    member.tell()

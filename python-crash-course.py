# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print(7**4)

s="Hi there Sam!"
print(s.split())

planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometres".format(planet,diameter))

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3]);

def domainGet(url):
    return url.split('@')[1];
print(domainGet('user@domain.com'))

def findDog(line):
    return 'dog' in line;
print(findDog('Is there a dog here?'))

def countDog(line):
    return line.count('dog');
print(countDog('This dog runs faster than the other dog dude!'))

seq = ['soup','dog','salad','cat','great']

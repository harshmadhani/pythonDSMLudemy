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
print(d['k1'][3]['tricky'][3]['target'][3])

def domainGet(url):
    return url.split('@')[1];
print(domainGet('user@domain.com'))

def findDog(line):
    return 'dog' in line.lower().split()
print(findDog('Is there a dog here?'))

def countDog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1
    return count
print(countDog('This dog runs faster than the other dog dude!'))

seq = ['soup','dog','salad','cat','great']
print(list(filter(lambda word : word[0] == 's' ,seq)))

def caught_speeding(speed, is_birthday):
    if is_birthday == True:
        count = 5
    else:
        count = 0
    if speed <= (60+count):
        return "No Ticket"
    elif speed >= (61+count) and speed <= (80+count):
        return "Small Ticket"
    else:
        return "Big Ticket"
print(caught_speeding(81,True))
print(caught_speeding(81,False))

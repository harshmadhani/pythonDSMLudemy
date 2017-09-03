# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 13:35:38 2017

@author: Harsh
"""

import numpy as num
print(num.zeros(10))
print(num.ones(10))
print(num.ones(10)*5)
print(num.arange(10,51))
print(num.arange(10,51,2))
print(num.arange(0,9).reshape(3,3))
print(num.eye(3))
print(num.random.rand(1))
print(num.random.randn(25))
print(num.linspace(0,1,100).reshape(10,10))
print(num.linspace(0,1,20))

mat = num.arange(1,26).reshape(5,5)
print(mat)
print(mat[2:,1:])
print(mat[3,4])
print(mat[:3,1].reshape(3,1))
print(mat[4])
print(mat[3:])
print(num.sum(mat))
print(num.std(mat))
print(num.sum(mat,axis=0))
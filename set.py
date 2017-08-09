#!/usr/bin/python3
# -*- coding: utf-8 -*-

x = set('spam')
y = {'h', 'a', 'm'}
print(x & y)
print(x | y)
print(x - y)
print({x**2 for x in [1,2,3,4]})
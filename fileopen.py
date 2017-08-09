#!/usr/bin/python3
# -*- coding: utf-8 -*-

f = open('data.txt', 'w')
f.write('Hello\n')

f.write('world')
f.close()


f = open('data.txt', 'rb')
text = f.read()
print(text)


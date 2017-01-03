#!/usr/bin/env python

i = raw_input('input a number : ')
i = int(i)
while i < 0 or i > 100 :
    print('input error')
    i = raw_input('input a number : ')

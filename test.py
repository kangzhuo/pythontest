#!/usr/bin/env python
# -*- coding: utf8 -*-

import hello

def cmpNum(x, y):
    x = int(x)
    y = int(y)
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0

class kb6:
    def strs2Nums(self, strs):
        n = []
        for str in strs:
            n.append(int(str))
        return n

    def sortNum(self):
        nums = raw_input('input num sort by num: ')
        nums = nums.split(',')
        print type(nums[0])
        nums.sort(cmp=cmpNum)
        print nums
        nums = self.strs2Nums(nums)
        print sum(nums)

    def strip(self):
        str = raw_input('input str for strip: ')
        print len(str)
        str.replace(' ','')
        print str

if __name__ == '__main__':
    print 'test main run'
    a = kb6()
    a.strip()

if __name__ == 'test':
    print 'test call'
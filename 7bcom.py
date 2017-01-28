# -*- coding:utf-8 -*-
from __future__ import division
import binascii,time

def decimal2hex(in_num):
    print bin(in_num)
    bin_raw=bin(in_num).split('0b')[1]
    bin_string_com=[]
    seg_id=0
    while len(bin_raw)<>0:
        ops_bin_str=bin_raw[-7:]
        # if seg_id==0: #插入1
        if len(ops_bin_str)<7:
            tmp_zero=[]
            for i in range(0,7-len(ops_bin_str)):
                tmp_zero.append('0')
            ops_bin_str=''.join(tmp_zero)+ops_bin_str
        if seg_id==0:
            ops_bin_str='0'+ops_bin_str
        else:
            ops_bin_str='1'+ops_bin_str
        bin_string_com.insert(0,ops_bin_str)
        bin_raw=bin_raw[:-7]
        seg_id+=1
    print bin_string_com
    print eval('0b'+''.join(bin_string_com))
    print hex(eval('0b'+''.join(bin_string_com)))

    return hex(eval('0b'+''.join(bin_string_com)))

def hex2decimal(in_num): #0x8a2d
    # print int('0x'+in_num_string,2)
    print bin(in_num)
    bin_raw=bin(in_num)
    bin_string=str(bin_raw).split('b')[1]
    bin_string_seg_length=int(len(bin_string)/8)
    bin_string_com=[]
    for i in range(0,bin_string_seg_length):
        bit_seg= bin_string[i*8:(i+1)*8]
        print bit_seg,bit_seg[1:8]
        bin_string_com.append(bit_seg[1:8])
    print eval('0b'+''.join(bin_string_com))

    return eval('0b'+''.join(bin_string_com))

hex2decimal(0x80819545)
# decimal2hex(93480)
# print bin('0b0010')
# -*- coding: utf-8 -*-
# @Time : 2020/5/19 16:47
# @Author : Fan
import itertools as its
import time
words = 'abcdefghijklmnopqrstuvwxyz1234567890'
#取8位
r = its.product(words,repeat=8)
dic = open(r'密码.txt','w')

for i in r:
    time.sleep(1)
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()
print('密码本已生成')
'''
mylist=("".join(x) for  x in  its.product("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",repeat=16))
while True:
    print(next(mylist))
'''

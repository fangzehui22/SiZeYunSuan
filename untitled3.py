# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 12:53:47 2018

@author: lenovo
"""


import random
opr = ['＋','－','×','÷']
ch = '0'
print('输入 "exit" 退出')
while True:
    fh = random.randint(0, 3) 
    n1 = random.randint(1, 10) #1<n1<10
    n2 = random.randint(1, 10) #1<n2<10
    rjg = 0
    if fh == 0:    #加
        rch = n1 + n2
    elif fh == 1:  #减
        n1,n2 = max(n1,n2),min(n1,n2) #确保用大的数减去小的数
        rch = n1 - n2
    elif fh == 2:  #乘
        rch = n1 * n2
    elif fh == 3:  #除
        n1,n2 = max(n1,n2),min(n1,n2)
        while n1 % n2 != 0:
            n1 = random.randint(1, 10)
            n2 = random.randint(1, 10)
            n1,n2 = max(n1,n2),min(n1,n2)
        rch = int(n1 / n2)
 
    print(n1, opr[fh], n2, '= ', end='')#自动生成题目
    ch = input()  #用户答案
    if ch == 'exit':  #输入exit则退出
        break
    sr = int(ch)
    if int(sr) == rch:
        print('√')
    else:
        print('×，答案：', rch)
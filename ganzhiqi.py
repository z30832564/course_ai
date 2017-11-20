# -*- coding: utf-8 -*-
import numpy as np
data = np.array([[180, 70],
        [179, 72],
        [165, 55],
        [161, 50]])
label = [1, 1, 0, 0]
def f(n):
    if n >= 0:
        return 1
    else:
        return 0

def jiance(a, b):
    flag = 1
    for i in range(0, len(a)):
        if a[i] == b[i]:
            pass
        else:
            flag = 0
    if flag == 1:
        return 0
    else:
        return 1

w0 = [0, 0]
b0 = 0
flag1 = 1
count = 1
while(flag1):
    a = []
    for i in range(0, 4):
        print('第', count, '次迭代：')
        num = np.dot(w0, data[i].T)+b0
        a.append(f(num))
        e = label[i]-f(num)
        print('a=', a[i])
        print('e=', e)
        if e == 0:
            pass
        else:
            w0 = w0+np.dot(e,data[i].T)
            b0 = b0+e
        count = count +1
        print('w:', w0)
        print('b:', b0)
    flag1 = jiance(a, label)
    print('**************************')
    print(a)
    print(w0)
    print(b0)
    print('**************************')
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:06:47 2016

@author: carter
"""
import string
#读字符串

#输入
m = raw_input()
s = m.split()

#检测输入格式
def judge(s):
    for i in range(len(s)):
        if s[i] == ',' or s[i] == '->' or s[i] == '(':
            if s[i + 1].islower():
                continue
            elif s[i + 1] == '(':
                continue
            else:
                print('输入有错误')
                break
judge(s)

def parenthesesANDcontains(s):
    list = []
    for i in range(0, len(s)):
        if s[i] == '(':
            list.append(1)
        elif s[i] == ')':
            list.append(-1)
        elif s[i] == '->':
            list.append(2)
        else:
            list.append(0)
    return list
pl = parenthesesANDcontains(s)
print pl

def findmid(s1):
    indexof2 = []
    s = parenthesesANDcontains(s1)
    for i in range(len(s)):
        if s[i] == 2:
            indexof2.append(i)
    for i in indexof2:
        sum1 = sum2 = 0
        for j in range(0, i):
            if s[j] != 2:
                sum1 = sum1+s[j]
        for j in range(i+1, len(s)):
            if s[j] != 2:
                sum2 = sum2+s[j]

        if sum1 == 0 and sum2 == 0:
            break
    return i

mid = findmid(s)
print mid


def firstchange(s, mid):
    l = []
    r = []
    for i in range(0, mid):
        l.append(s[i])
    for i in range(0, mid):
        del s[i]
    del s[mid]
    r = s
    if l[0] == '(' and l[-1] == ')':
        del l[0]
        del l[-1]
    if r[0] == '(' and l[-1] == ')':
        del r[0]
        del r[-1]
    return l, r
l, r = firstchange(s, mid)
print l, r



# 规则1 若 a ,!X,b => r  则 a, b =>X,r
def change(l, r, flag):
    for i in range(0, len(l)):
        if l[i] == '!':
            if l[i+1] == '(':
                o = []
                k = -1
                h = 0
                for j in range(i+1, len(l)):
                    o.append(l[j])
                    if l[j] == ')':
                        k = k+1
                    elif h==1 and l[j] == '(':
                        k = k-1
                    l[j] = 0
                    h=1
                    if k == 0:
                        break
                l = filter(None,l)
                r.append(',')
                r.extend(o)
            elif l[i+1].islower():
                p = []
                p.append(l[i+1])
                del l[i+1]
                r.append(',')
                r.extend(p)
            if flag == 1:
                del l[i], l[i]
            else:
                del l[i], l[i]
            break
    return l, r
# 规则1 若 a ,!X,b => r  则 a, b =>X,r
def lawone(l,r):
    return change(l, r, 1)
# 规则2 若 a ,b =>!X, r  则 a, X, b =>r
def lawtwo(l,r):
    l_, r_ = change(r, l, 2)
    return r_, l_


# 规则3 若a,(X -> Y), b =>r 则 a, X,b=>r且a,Y,b=>r
def lawthree(l,r):
    lk = parenthesesANDcontains(l)
    for i in range(0, len(lk)):
        if lk[i] = 2:
            k = []
            suml = sumr =0
            for p in range(i-1, -1):
                if p == 0:break
                elif lk[p] == -1 and lk[p-1] == 0:break
                else:
                    if lk[p] != 2:
                        suml = suml + lk[p]
                        if lk[p] == -1
            for q in range(i+1, len(lk)):
                if p == len(lk):break
                elif lk[p] == 1 and lk[p+1] == 0:break
                else:
                    if lk[p] != 2: sumr = sumr + lk[p]
            if suml == sumr and suml ==0:



'''
l = raw_input()
r = raw_input()
l = l.split()
r = r.split()

s, p = lawtwo(l, r)
print s
print p
'''
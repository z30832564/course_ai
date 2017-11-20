# -*- coding: utf-8 -*-
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
#返回逗号的位置
def dou(s):
    dou = []
    for i in s:
        if s[i] == ',':
            dou.append(i)
    return dou
def lawthree(l,r):
    lk = parenthesesANDcontains(l)
    print lk
    placeofdou = dou(l)
    for i in range(0, len(lk)):
        if lk[i] == 2:
            suml = sumr =0
            for p in range(i-1, -1, -1):
                if p == 0:
                    if lk[p] == 1:
                        suml = suml + lk[p]
                    break
                if lk[p] == 1 and lk[p-1] == 0:
                    suml = suml + lk[p]
                    break
                else:
                    if lk[p] != 2:
                        suml = suml + lk[p]
            for p in range(i+1, len(lk)):
                if p == len(lk):
                    if lk[p] == -1:
                        sumr = sumr + lk[p]
                    break
                if lk[p] == -1 and lk[p+1] == 0:
                    sumr = sumr + lk[p]
                    break
                else:
                    if lk[p] != 2:
                        sumr = sumr + lk[p]
            print suml,sumr
            if suml ==0 and sumr == 0:print 'lllllll'
            elif suml+sumr == 0:print '2222'






l = raw_input()
r = raw_input()
l = l.split()
r = r.split()

lawthree(l, r)
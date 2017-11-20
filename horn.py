# -*- coding: utf-8 -*-
'''

title:在一阶逻辑框架内对horn子句的归结
date:2017.9.5
author:carter

'''
def input():
    print '输入要归结的子句个数：'
    num = raw_input()
    num = int(num)
    flag = 0
    jihe = []
    _jihe = []
    n = 0
    print '请依次输入子句，析取由‘|’表示：'
    while n < num:
        #print '[', n+1, ']:'
        k = []
        s = raw_input()
        k = s.split('|')
        jihe.append(k)
        n = n+1
    _jihe = jihe[:]
    print '输入的子句有：'
    for i in range(0, len(jihe)):
        print i+1, ':', jihe[i]
    print '***************************'
    return jihe, _jihe
'''
def remove_(s, c):
    a = s.find(c)
    s = list(s)
    del s[a:a+len(c)]
    return s
'''
def guijie(s, c):
    #子句1没有！的情况
    c = list(c)
    ceng = 0
    #print len(s)
    for y in range(len(s)-1, -1, -1):
        s[y] = list(s[y])
        # print ceng
        if '!' not in s[y]:
            for u in c:
                if '!' not in u:
                    #print '!not'
                    continue
                else:
                    if s[y][0] not in u:
                        #print 'not'
                        continue
                    else:
                        c.remove(u)
                        s.remove(s[y])
                        #print c
                        #print s
        # 子句1 中有！的情况
        elif '!' in s[y]:
            for u in c:
                if '!' in u:
                    #print '!not'
                    continue
                else:
                    if s[y][1] not in u:
                        #print 'not'
                        continue
                    else:
                        c.remove(u)
                        s.remove(s[y])
                        #print c
                        #print s
        ceng = ceng +1
    # print c
    # print s
    return s, c

def count(jihe):
    return len(jihe)

def judge(jihe):
    flag2 = 0
    for i in jihe:
        if len(jihe[i]) != 0:
            flag =1
    return flag2


jihe, jihe1 = input()

# s, c = guijie(['p(a)', 'q(b)', '!o(d)'], ['!p(y)', 'r()', '!q(a)', 't', 'o(d)'])
# print s, c
def main():
    flag = 1
    while flag == 1:
        #print jihe1
        for i in range(len(jihe)-1, -1, -1):
            for j in range(len(jihe)-1, -1, -1):
                if i != j:
                    for y in jihe[i]:
                        flag1 = 1
                        y = list(y)
                        for u in jihe[j]:
                            if y[0] in u and '!' in u:
                                u = list(u)
                                #print u
                                vv = u.index(y[0])
                                if vv == 1:
                                    flag1 = 0
                                #print flag1
                            if y[1] in u and '!' not in u:
                                u = list(u)
                                vv = u.index(y[1])
                                if vv == 0:
                                    flag1 = 0
                                #print flag1
                    # print '选择这两个子句', jihe[i], jihe[j]
                    if flag1 == 0:
                        s, c = guijie(jihe[i], jihe[j])
                        if len(s) != 0:
                            nn = count(jihe1) + 1
                            mm = jihe1.index(jihe[i])
                            bb = jihe1.index(jihe[j])
                            print nn, c, '    由', mm+1, '和', bb+1, '得'
                            #print jihe1
                            jihe1.append(s)
                            #print jihe1
                            jihe[i] = s
                        if len(c) != 0:
                            nn = count(jihe1) + 1
                            mm = jihe1.index(jihe[i])
                            bb = jihe1.index(jihe[j])
                            print nn, c, '    由', mm+1, '和', bb+1, '得'
                            #print jihe1
                            jihe1.append(c)
                            #print jihe1
                            jihe[j] = c
                        if len(c) == 0 and len(s) == 0:
                            nn = count(jihe1) + 1
                            mm = jihe1.index(jihe[i])
                            bb = jihe1.index(jihe[j])
                            print nn+1, c, '    由', mm+1, '和', bb+1, '得'
                            print '可以由归结得到'
                            flag = 0
                            break

        print '------------------------------'

main()
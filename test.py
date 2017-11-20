# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:06:47 2016

@author: dell
"""
import copy


# 列表转字符串
def listtostr(m):
    s = ''
    for i in m:
        s = s + i + ' '
    return s


print '请输入要推理的字符串(字符之间用空格做间隔):'
s = raw_input()
s = '=>' + ' ' + s
m = s.split()


# 检测函数
def strerro(m):
    for i in range(len(m)):
        if m[i] == ',' or m[i] == '->' or m[i] == '=>':
            if m[i + 1].islower():
                continue
            elif m[i + 1] == '(':
                continue
            else:
                print('输入有错误')
                break


strerro(m)


# 识别最外层括号，返回左右括号位置的列表的汇总列表
def kuohao(m):
    o = []
    p = []
    kuolist = []
    for i in range(len(m)):
        if m[i] == '(':
            o.append(-1)
            p.append(i)
        elif m[i] == ')':
            o.append(1)
            p.append(i)
        else:
            continue
        t = sum(o)
        if t == 0:
            kuolist.append([p[0], p[-1]])
            o = []
            p = []
    return kuolist


# 识别最外层逗号，返回最外层逗号的位置列表
def douhao(m):
    doulist = [-1]  # 为字符串开头加一标志位
    for i in range(len(m)):
        if m[i] == ',' or m[i] == '=>':  # 逗号和相继式符号位置添加到逗号列表
            doulist.append(i)
    return doulist


# 识别最外层符号
def jiance(dm):
    dmkuo = kuohao(dm)
    if dm[0] == '!':
        return 1
    elif dm[1] == '->':
        return 2
    elif dm[dmkuo[0][-1] + 1] == '->':
        return 2


def find_(m, doulist):
    t = m.index('=>')
    if doulist[1] - 1 == doulist[0]:
        doulist.pop(0)
    # print doulist
    k = 0
    for i in doulist:
        if i + 2 == len(m) or m[i + 2] == ',' or m[i + 2] == '=>':
            # print('单一元素位置：\n',m[i+1:i+2],i+1)
            k = k + 1
            continue
        if doulist[k] == doulist[-1]:
            last = len(m)
        else:
            last = doulist[k + 1]
        dm = m[i + 1:last]
        print '要处理的子段是：\n', listtostr(dm)
        dou = last
        j = jiance(dm)
        if j == 1:
            if i < t:
                return feileft(dm, m, dou - 1, i)
            elif i >= t:
                return feiright(dm, m, dou - 1, i)
            break
        elif j == 2:
            if i < t:
                return yunleft(dm, m, dou - 1, i)
            elif i >= t:
                return yunright(dm, m, dou - 1, i)
            break
        k = k + 1


# 处理逗号
def dd(m):
    for i in range(len(m)):
        if i == len(m) - 1:
            if m[i] == ',':
                m.pop()
            break
        elif m[i] == ',' and m[i + 1] == ',':
            m.pop(i)
    return m


# 处理重复逗号的情况
def deal(dou, i):
    for x in range(dou, i, -1):
        if x == '=>':
            continue
        m.pop(x)
    return m


# 返回蕴含符号位置
def yunhan(ss):
    dmkuo = kuohao(ss)
    if ss[1] == '->':
        return 1
    else:
        return dmkuo[0][-1] + 1


# 按照四种情况处理 M 列表
# 规则1 若 a ,!X,b => r  则 a, b =>X,r
def feileft(ss, m, dou, i):
    ss.pop(0)
    kuoss = kuohao(ss)
    if kuoss != []:
        ss.pop(0)
        ss.pop(-1)
    t = m.index('=>')
    if t != 0:
        m.append(',')
    m.extend(ss)
    m = deal(dou, i)
    if m[0] == ',':
        m.pop(0)
    m = dd(m)
    # print('\n"!"在"=>"左边\n', '-------m-------\n',listtostr(m))
    return [[m, '规则1', ' ', [0]]]


# 规则2 若 a ,b =>!X, r  则 a, X =>b , r
def feiright(ss, m, dou, i):
    ss.pop(0)
    kuoss = kuohao(ss)
    if kuoss != []:
        ss.pop(0)
        ss.pop(-1)
    m = deal(dou, i)
    for x in range(len(m)):
        if x == len(m) - 1:
            break
        elif m[x] == '=>' and m[x + 1] == ',':
            m.pop(x + 1)
            break
    t = m.index('=>')
    if t != 0:
        m.insert(0, ',')
    ss.reverse()
    for i in ss:
        m.insert(0, i)

    m = dd(m)
    # print('\n"!"在"=>"右边\n','-------m-------\n',listtostr(m))
    return [[m, '规则2', ' ', [0]]]


# 规则3 若 a ,(X -> Y),b => r  则 a ,!X,b => r ; a ,Y,b => r

def yunleft(ss, m, dou, i):
    yun = yunhan(ss)
    ssx = ss[:yun]
    ssy = ss[yun + 1:]
    ssx.insert(0, '!')
    kuossy = kuohao(ssy)
    if kuossy != []:
        ssy.pop(0)
        ssy.pop(-1)
    m = deal(dou, i)
    m1 = copy.deepcopy(m)
    m2 = copy.deepcopy(m)
    t = m.index('=>')
    if t != 0:
        m1.insert(0, ',')
        m2.insert(0, ',')
    ssx.reverse()
    ssy.reverse()
    for i in ssx:
        m1.insert(0, i)
    for i in ssy:
        m2.insert(0, i)
    m1 = dd(m1)
    m2 = dd(m2)
    # print('\n"->"在"=>"左边\n',\
    # '--------m1-------\n',listtostr(m1),\
    # '\n--------m2-------\n',listtostr(m2))
    # return listtostr(m1),listtostr(m2)
    return [[m1, '规则3', ' ', [0]], [m2, '规则3', ' ', [0]]]


# 规则4 若 a => b, (X -> Y), r  则 a => b, ！X ， Y , r

def yunright(ss, m, dou, i):
    yun = yunhan(ss)
    ssx = ss[:yun]
    ssy = ss[yun + 1:]
    ssx.insert(0, '!')
    kuossy = kuohao(ssy)
    if kuossy != []:
        ssy.pop(0)
        ssy.pop(-1)
    ssxy = ssx + [','] + ssy
    for x in range(dou, i, -1):
        if x == '=>':
            continue
        m.pop(x)
    t = m.index('=>')
    if m[t] != m[-1] and m[t + 1] == ',':
        m.pop(t + 1)
    if m[-1] != '=>':
        m.append(',')
    m.extend(ssxy)
    m = dd(m)
    # print('\n"->"在"=>"右边\n','-------m-------\n',listtostr(m))
    return [[m, '规则4', ' ', [0]]]


# 处理过程
e = 0
stock = []
stock.append([m, '结果', ' ', [0]])
stock1 = []
while (stock):
    e = e + 1
    y = 0
    print '\t\t*****', e, '*****'
    mm = stock.pop()
    m = mm[0]
    if '->' not in m and '!' not in m:
        d = m.index('=>')
        m1 = m[:d]
        m2 = m[d + 1:]
        for i in m1:
            if i != ',':
                if i in m2:
                    print listtostr(m).decode('utf-8'), '公理', '\n -------END------'
                    stock1.append([listtostr(m), mm[1], '公理', mm[3]])
                    break
                else:
                    y = y + 1
        for i in m1:
            if i == ',':
                m1.remove(i)
        if y == len(m1):
            print listtostr(m), '不是公理', '\n -------END------'
            stock1.append([listtostr(m), mm[1], '不是公理', mm[3]])
            break
        continue
    stock1.append([listtostr(m), mm[1], mm[2], mm[3]])
    print '要处理的字符串:\n', listtostr(m)
    kuolist = kuohao(m)
    doulist = douhao(m)
    f = find_(m, doulist)
    print '处理后的结果:\n'
    for i in range(len(f)):
        f[i][3] = [mm[3][0] + i]
        print listtostr(f[i][0]), f[i][1], '\n -------END------'
        stock.append(f[i])

# 输出过程
k = []
for i in range(len(stock1)):
    k.append([len(stock1) - i, stock1[i][3][0]])


# 查找由规则3分出来的两个字符串
def rdo(bb):
    q = []
    for i in range(len(bb)):
        if i + 1 == len(bb) - 1:
            if bb[i][1] == bb[i - 1][1]:
                break
        if bb[i][1] == bb[i + 1][1]:
            continue
        else:
            for j in range(i, len(bb)):
                if bb[j][1] not in [x[1] for x in bb[i + 1:len(bb)]]:
                    t = [0, 0]
                    break
                if bb[j + 1][1] == bb[i][1]:
                    t = bb[j + 1]
                    break
            q.append([bb[i][0], t[0], bb[i][0] - 1])
    return q


q = rdo(k)
q.reverse()
stock1.reverse()
for i in range(len(stock1)):
    if i + 1 in [j[0] for j in q]:
        for j in q:
            if i + 1 == j[0]:
                stock1[i][3] = [j[1], j[2]]
                continue
    else:
        stock1[i][3] = [i]

print('\n推理过程：\n')
b = []
a = 0
for i in range(len(stock1)):
    a = a + 1
    if stock1[i][2] == '不是公理':
        print('式子不能由推理得到')
        break
    elif stock1[i][2] == '公理':
        print '[', a, ']', '{:<60}'.format(stock1[i][0]), '\t', '{:<10}'.format(stock1[i][2])
    else:
        print '[', a, ']', '{:<60}'.format(stock1[i][0]), '\t', '{:<10}'.format('由' + str(stock1[i][3]) + '和' + stock1[i - 1][1])

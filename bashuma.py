# -*- coding: utf-8 -*-
import numpy as np
import copy
'''
#初始化棋盘
print '初始化棋盘：'
chess = np.array([[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
                  )
for i in range(0, len(chess)):
    for j in range(0, len(chess[0])):
        print '第', i+1, '行 ', j+1, '列:'
        chess[i][j] = raw_input()
print chess

#输入目标棋盘
print '目标棋盘：'
chess_f = chess = np.array([[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]])
for i in range(0, len(chess_f)):
    for j in range(0, len(chess_f[0])):
        print '第', i+1, '行 ', j+1, '列:'
        chess_f[i][j] = raw_input()
print chess_f

'''
chess = np.array([[2, 8, 3],
                  [1, 6, 0],
                  [7, 5, 4]])
print chess
chess_f = np.array([[1, 2, 3],
                  [8, 0, 4],
                  [7, 6, 5]])
#计算w(n)的函数
def W(chess, chess_f):
    w = 0
    for i in range(0, len(chess_f)):
        for j in range(0, len(chess_f[0])):
            if chess[i][j] !=0:
                if chess[i][j] == chess_f[i][j]:
                    w = w + 1
    return 8-w



#计算p(n)的函数
def P(chess, chess_f):
    p = 0
    for i in range(0, len(chess_f)):
        for j in range(0, len(chess_f[0])):
            if chess[i][j] != 0:
                if chess_f[i][j] != chess[i][j]:
                    #寻找相同数的位置
                    for x in range(0, len(chess_f)):
                        for y in range(0, len(chess_f[0])):
                            if chess_f[x][y] == chess[i][j]:
                                p = p + abs(x-i) + abs(y-j)
    return p


#向上、下、左、右移

def UP(chess):
    chess0 = copy.copy(chess)
    i = 0
    j = 0
    for x in range(0, len(chess0)):
        for y in range(0, len(chess0[0])):
            if chess0[x][y] == 0:
                i = x
                j = y
    if i != 0:
        chess0[i][j] = chess0[i-1][j]
        chess0[i-1][j] = 0
    return chess0

def DOWN(chess):
    chess0 = copy.copy(chess)
    i = 0
    j = 0
    for x in range(0, len(chess0)):
        for y in range(0, len(chess0[0])):
            if chess0[x][y] == 0:
                i = x
                j = y
    if i < (len(chess)-1):
        chess0[i][j] = chess0[i + 1][j]
        chess0[i + 1][j] = 0
    return chess0

def LEFT(chess):
    chess0 = copy.copy(chess)
    i = 0
    j = 0
    for x in range(0, len(chess0)):
        for y in range(0, len(chess0[0])):
            if chess0[x][y] == 0:
                i = x
                j = y
    if j !=0:
        chess0[i][j] = chess0[i][j-1]
        chess0[i][j-1] = 0
    return chess0

def RIGHT(chess):
    chess0 = copy.copy(chess)
    i = 0
    j = 0
    for x in range(0, len(chess0)):
        for y in range(0, len(chess0[0])):
            if chess0[x][y] == 0:
                i = x
                j = y
    if j < (len(chess0[0])-1):
        chess0[i][j] = chess0[i][j + 1]
        chess0[i][j + 1] = 0
    return chess0

def nextstep(chess, chess_s):
    chess_0 = UP(chess)
    chess_1 = DOWN(chess)
    chess_2 = LEFT(chess)
    chess_3 = RIGHT(chess)
    c = []
    if(~(chess_0 == chess).all() and ~(chess_0 == chess_s).all()):
        c.append(chess_0)
    if (~(chess_1 == chess).all() and ~(chess_1 == chess_s).all()):
        c.append(chess_1)
    if (~(chess_2 == chess).all() and ~(chess_2 == chess_s).all()):
        c.append(chess_2)
    if (~(chess_3 == chess).all() and ~(chess_3 == chess_s).all()):
        c.append(chess_3)
    return c

def judge_the_min(open_value):
    index = []
    for i in range(0, len(open_value)):
        min1 = min(open_value)
        index.append(open_value.index(min1))
        open_value[open_value.index(min1)] = 1000
        min2 = min(open_value)
        if min2 > min1:
            break

    return index

















'''
open = []
open_value_w = []
open_value_p = []
open_count = []
chess_g = chess
chess_s = chess
count = 1
flag = 1
the_step = []
while(flag):
    print '第',count,'层'
    c = nextstep(chess_g, chess_s)
    #for i in c:
        #if (i == chess_f).all():
            #flag = 0
            #break
    for i in range(0, len(c)):
        #open.insert(0, c[i])
        open_value_w.insert(0, W(c[i], chess_f))
        #open_count.insert(0, count)
    d = judge_the_min(open_value_w)
    #d = judge_the_min(open_value)
    if len(d) == 1:
        print '选定节点：'
        print c[d[0]]
        the_step.append(c[d[0]])
    elif len(d) > 1:
        for r in d:
            open_value_p.insert(0, P(c[i], chess_f))

        print open_value_p
        print min(open_value_p)
        the_step.append(c[d[min(open_value_p)]])
    if count > 1:
        chess_s = chess_g



    chess_g = the_step[-1]
    #count = open_count[d]
    #del open[d]
    #del open_value[d]
    #del open_count[d]

    print 'open表:\n',open
    print 'open表值:\n',open_value
    if flag == 0:
        break

    count = count + 1
    print '***********************************************************************'


print '共需',count,'步'
print chess
for i in np.array(the_step):
    print i
    print '    |'
    print '    |'
print chess_f


'''




list_chess = []
list_chess.append(chess)
k = 1
chess_g = chess
the_step = []
flag = 5
open = []
open.append(chess)
while(flag):
    print '第', k, '层'
    print list_chess
    the_step.append(list_chess)
    list_value = []
    list_chess_ = []
    for chess in list_chess:
        #print chess
        chesses_q = nextstep(chess, chess_g)

    
        for q in np.array(chesses_q):
            ff = 0
            for opens in open:
                if((opens == q).all()):
                    ff = 1
                    print 'yanzheng:',q
                    break
            if(ff == 0):
                list_value.append(P(q, chess_f) + k)
                list_chess_.append(q)
                open.append(q)
        print list_chess_
        print list_value



    min_list = []
    for i in list_value:
        min_1 = min(list_value)
        a = list_value.index(min_1)
        list_value[a] = 100
        min_2 = min(list_value)
        min_list.append(a)
        if min_1 < min_2:
            break

    print min_list


    list_internative = []
    for i in min_list:
        print list_chess_[i]
        list_internative.append(list_chess_[i])

    print open
    for chess in list_chess_:
        if((chess == chess_f).all()):
            flag = 0
            break
    if k>1:
        chess_g = chesses_q[min_list[0]]

    list_chess = list_internative
    k = k+1

print '共需',k-1,'步'
print chess
for i in np.array(the_step):
    print i
print chess_f



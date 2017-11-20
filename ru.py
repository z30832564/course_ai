# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 15:22:36 2016

@author: asus
"""
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import io
Pb = 0.10
Pj = 0.85

filename = io.open("city")
li, xi, yi = np.loadtxt(filename, unpack='true')

leng = len(li)
for i in range(leng):
    li[i] = li[i] - 1
ran = np.ones((60, leng))


def rand(li):
    for i in range(60):
        random.shuffle(li)
        ran[i] = li
    return


rand(li)

'''
计算两点间的距离
'''


def distance(a, b, c):
    return math.sqrt((xi[int(ran[a][b])] - xi[int(ran[a][c])]) * (xi[int(ran[a][b])] - xi[int(ran[a][c])]) + (
    yi[int(ran[a][b])] - yi[int(ran[a][c])]) * (yi[int(ran[a][b])] - yi[int(ran[a][c])]))


'''
找出种群中最短的路径并在显示在图中
'''


def mplot(ran):
    a = list(range(0, 60))
    b = 0.0
    for i in range(60):
        for j in range(leng - 1):
            b = b + distance(i, j, j + 1)
        b = b + distance(i, 0, leng - 1)
        a[i] = b
        b = 0.0
    for k in range(60):
        if a[k] == min(a):
            b = k
            break
    x = list(range(0, leng))
    y = list(range(0, leng))
    for p in range(leng):
        x[p] = xi[int(ran[b][p])]
        y[p] = yi[int(ran[b][p])]
    plt.plot(x, y, '-or')
    plt.show()
    return a[b]


'''
遗传算法中的选择
'''


def select(ran, exten):
    a = list(range(0, 60))
    b = 0.0
    for i in range(60):
        for j in range(leng - 1):
            b = b + distance(i, j, j + 1)
        b = b + distance(i, 0, leng - 1)
        a[i] = b
        b = 0.0
    for k in range(60):
        if a[k] == max(a):
            b = k
            break
    c = 0.0
    for p in range(len(exten)):
        '''if int(exten[p][0])==1 and int(exten[p][1])==1:
            break'''
        for q in range(leng - 1):
            c = c + distance(p, q, q + 1)
        c = c + distance(p, 0, leng - 1)
        if c < a[b]:
            ran[b] = exten[p]
        else:
            Ph = random.random()
            if Ph < 0.095:
                ran[b] = exten[p]
        c = 0.0
    return


'''
遗传算法中的交叉
'''


def cross(ran):
    exten = np.ones((2, leng))
    a = list(range(0, 60))
    random.shuffle(a)
    for i in range(1, 31):
        b = random.random()
        if b < Pj:
            x = random.randint(0, leng - 1)
            y = random.randint(0, leng - 1)
            while x == y:
                y = random.randint(0, leng - 1)
                if x != y:
                    break
            if x > y:
                x, y = y, x
            exten[0] = ran[a[i * 2 - 1]]
            exten[1] = ran[a[i * 2 - 2]]
            for f in range(x, y + 1):
                exten[0][f], exten[1][f] = exten[1][f], exten[0][f]
            judge = 0
            for g in range(0, leng):
                for h in range(x, y + 1):
                    if (g < x or g > y) and exten[0][g] == exten[0][h]:
                        for j in range(0, leng):
                            for k in range(x, y + 1):
                                if (j < x or j > y) and exten[1][j] == exten[1][k]:
                                    exten[0][g], exten[1][j] = exten[1][j], exten[0][g]
                                    judge = 1
                                    break
                            if judge == 1:
                                judge = 0
                                break
            select(ran, exten)
    return


'''
遗传算法中的变异
'''


def change(ran):
    exten = np.ones((1, leng))
    for i in range(60):
        a = random.random()
        if a < Pb:
            x = random.randint(0, leng - 1)
            y = random.randint(0, leng - 1)
            while x == y:
                y = random.randint(0, leng - 1)
                if x != y:
                    break
            exten[0] = ran[i]
            exten[0][x], exten[0][y] = exten[0][y], exten[0][x]
            select(ran, exten)
    return


'''
主函数
'''


def main():
    i = 200
    while (i > 0):
        cross(ran)
        change(ran)
        i = i - 1
    return


print("最初路径图：")
print("最初种群中最短路径值为：%f" % mplot(ran))
main()
print("最短路径图：")
print("最终种群中最短路径值为：%f" % mplot(ran))
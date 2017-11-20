# -*- coding: utf-8 -*-
'''
Author:zy
'''

import pygame,sys,random
from pygame.locals import *
# pygame初识化
pygame.init()

#定义全局变量
white_x=[]
white_y=[]
black_x = []
black_y = []
logo=0

#定义棋盘状态，无子为-1，白子为0，黑子为1
chessboard=[[-1 for col in range(15)] for row in range(15)]
#print(chessboard)

#定义退出函数
def gomoku_exit():
    # 接受到退出指令后退出程序
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

#绘制棋盘，棋盘每个方格，长53，高53。
screen=pygame.display.set_mode((805,805))
pygame.display.set_caption("五子棋")
chessboard_back=pygame.image.load("chessboard.png").convert_alpha()
chessboard_back=pygame.transform.smoothscale(chessboard_back,(800,800))

#绘制棋子
white=pygame.image.load("white.png").convert_alpha()
black=pygame.image.load("black.png").convert_alpha()
white=pygame.transform.smoothscale(white,(35,35))
black=pygame.transform.smoothscale(black,(35,35))

def show_text(surface_handle, pos, text, color, font_bold=False, font_size=13, font_italic=False):
    '''
    Function:文字处理函数
    Input：surface_handle：surface句柄
           pos：文字显示位置
           color:文字颜色
           font_bold:是否加粗
           font_size:字体大小
           font_italic:是否斜体
    '''
    # 获取系统字体，并设置文字大小
    cur_font = pygame.font.SysFont("Calibri", font_size)
    # 设置是否加粗属性
    cur_font.set_bold(font_bold)
    # 设置是否斜体属性
    cur_font.set_italic(font_italic)
    # 设置文字内容
    text_fmt = cur_font.render(text, 1, color)
    # 绘制文字
    surface_handle.blit(text_fmt, pos)

#定义游戏获胜
def ShowWinScreen():
    show_text(chessboard_back,(15,350),"YOU WIN !!!",(255,0,0),True,130)

#定义游戏失败
def ShowLoseScreen():
    show_text(chessboard_back, (15, 350), "YOU LOSE !!", (255, 0, 0), True, 130)

'''
五子棋判断有多少相同棋子相连，i为横坐标，j为纵坐标，label为中心棋子的属性
返回值说明：
direction:0为横向，1为斜向下，2为纵向，3位斜向上
sum:多少相同棋子相连
flag（状态位）:0为左右皆为活，1为左死右活，2为左活右死，3为左右皆为死
'''
#判断横向棋子
def statistic_0(i,j):
    flag=0
    sum_0_right=0
    sum_0_left=0
    label=chessboard[i][j]
    for d in range(1,100):
        if i+d in range(15):
            if chessboard[i+d][j]==label:
                sum_0_right=sum_0_right+1
            elif chessboard[i+d][j]==1-label:
                flag=flag+2
            else:
                break
    for d in range(1,100):
        if i-d in range(15):
            if chessboard[i-d][j]==label:
                sum_0_left=sum_0_left+1
            elif chessboard[i-d][j]==1-label:
                flag=flag+1
            else:
                break
    sum_0=sum_0_right+sum_0_left+1
    #print(sum_0)
    return 0, sum_0, flag

#判断斜向下
def statistic_1(i,j):
    flag=0
    sum_1_right=0
    sum_1_left=0
    label=chessboard[i][j]
    for d in range(1,100):
        if i+d in range(15) and j+d in range(15):
            if chessboard[i+d][j+d]==label:
                sum_1_right=sum_1_right+1
            elif chessboard[i+d][j+d]==1-label:
                flag=flag+2
            else:
                break
    for d in range(1,100):
        if i-d in range(15) and j-d in range(15):
            if chessboard[i-d][j-d]==label:
                sum_1_left=sum_1_left+1
            elif chessboard[i-d][j-d]==1-label:
                flag=flag+1
            else:
                break
    sum_1=sum_1_right+sum_1_left+1
    #print(sum_1)
    return 1, sum_1, flag

#判断纵向
def statistic_2(i,j):
    flag=0
    sum_2_right=0
    sum_2_left=0
    label=chessboard[i][j]
    for d in range(1,100):
        if j-d in range(15):
            if chessboard[i][j-d]==label:
                sum_2_right=sum_2_right+1
            elif chessboard[i][j-d]==1-label:
                flag=flag+2
            else:
                break
    for d in range(1,100):
        if j+d in range(15):
            if chessboard[i][j+d]==label:
                sum_2_left=sum_2_left+1
            elif chessboard[i][j+d]==1-label:
                flag=flag+1
            else:
                break
    sum_2=sum_2_right+sum_2_left+1
    #print(sum_2)
    return 2, sum_2, flag

#判断斜向上
def statistic_3(i,j):
    flag=0
    sum_3_right=0
    sum_3_left=0
    label=chessboard[i][j]
    for d in range(1,100):
        if i-d in range(15) and j+d in range(15):
            if chessboard[i-d][j+d]==label:
                sum_3_right=sum_3_right+1
            elif chessboard[i-d][j+d]==1-label:
                flag=flag+2
            else:
                break
    for d in range(1,100):
        if i+d in range(15) and j-d in range(15):
            if chessboard[i+d][j-d]==label:
                sum_3_left=sum_3_left+1
            elif chessboard[i+d][j-d]==1-label:
                flag=flag+1
            else:
                break
    sum_3=sum_3_right+sum_3_left+1
    #print(sum_3)
    return 3, sum_3, flag

'''
博弈估价函数指标：
双活一          5000
活一死一         200
双死一             0
双活二         50000
活二死二        1000
双死二           100
双活三        180000
活三死三       30000
双死三           300
双活四        200000
活四死四      160000
双死四           500
'''
def estimate(sum,flag):
    grade=0
    if sum == 1 and flag == 0 :
        grade = 5000
    if sum == 1 and ( flag == 1 or flag == 2 ) :
        grade = 200
    if sum == 1 and flag == 3 :
        grade = 0
    if sum == 2 and flag == 0 :
        grade = 50000
    if sum == 2 and ( flag == 1 or flag == 2 ) :
        grade = 1000
    if sum == 2 and flag == 3:
        grade = 100
    if sum == 3 and flag == 0 :
        grade = 180000
    if sum == 3 and ( flag == 1 or flag == 2 ) :
        grade = 30000
    if sum == 3 and flag == 3:
        grade = 300
    if sum == 4 and flag == 0 :
        grade = 200000
    if sum == 4 and ( flag == 1 or flag == 2 ) :
        grade = 160000
    if sum == 4 and flag == 3:
        grade = 500
    return grade

#评价一个空点的分值,label为假设该点的属性
def analysis(i,j,label):
    chessboard[i][j]=label
    direction_0,sum_0,flag_0=statistic_0(i,j)
    direction_1,sum_1,flag_1=statistic_1(i,j)
    direction_2,sum_2,flag_2=statistic_2(i,j)
    direction_3,sum_3,flag_3=statistic_3(i,j)
    grade_0=estimate(sum_0,flag_0)
    grade_1=estimate(sum_1,flag_1)
    grade_2=estimate(sum_2,flag_2)
    grade_3=estimate(sum_3,flag_3)
    grade_total=grade_0+grade_1+grade_2+grade_3
    return grade_total

'''
人机博弈函数
0方向为水平向右，顺时针依次为1-7
'''
def game():
    #定义局部变量
    value=[]

    for i in range(15):
        for j in range(15):

            if chessboard[i][j] == 1:

                '''
                抑制人,益于电脑
                '''
                value_p = []
                #0方向
                if i+1 in range(15) and chessboard[i+1][j] == -1:
                    human_0=analysis(i + 1, j, 1)
                    computer_0 = analysis(i+1,j,0)
                    chessboard[i+1][j]=-1
                    total_0 = max(human_0, computer_0)
                    value_p.append([i+1,j,total_0])
                #1方向
                if i+1 in range(15) and j+1 in range(15) and chessboard[i+1][j+1] == -1:
                    human_1=analysis(i + 1, j+1, 1)
                    computer_1 = analysis(i+1,j+1,0)
                    chessboard[i+1][j+1]=-1
                    total_1 = max(human_1, computer_1)
                    value_p.append([i+1,j+1,total_1])
                #2方向
                if j+1 in range(15) and chessboard[i][j+1] == -1:
                    human_2=analysis(i, j+1, 1)
                    computer_2 = analysis(i,j+1,0)
                    chessboard[i][j+1]=-1
                    total_2 = max(human_2, computer_2)
                    value_p.append([i,j+1,total_2])
                #3方向
                if i-1 in range(15) and j+1 in range (15) and chessboard[i-1][j+1] == -1:
                    human_3=analysis(i - 1, j + 1, 1)
                    computer_3 = analysis(i-1,j+1,0)
                    chessboard[i-1][j+1]=-1
                    total_3 = max(human_3, computer_3)
                    value_p.append([i-1,j+1,total_3])
                #4方向
                if i-1 in range(15) and chessboard[i-1][j] == -1:
                    human_4=analysis(i - 1, j, 1)
                    computer_4 = analysis(i-1,j,0)
                    chessboard[i-1][j]=-1
                    total_4 = max(human_4, computer_4)
                    value_p.append([i-1,j,total_4])
                #5方向
                if i-1 in range(15) and j-1 in range(15) and chessboard[i-1][j-1] == -1:
                    human_5=analysis(i - 1, j - 1, 1)
                    computer_5 = analysis(i-1,j-1,0)
                    chessboard[i-1][j-1]=-1
                    total_5 = max(human_5, computer_5)
                    value_p.append([i-1,j-1,total_5])
                #6方向
                if j-1 in range(15) and chessboard[i][j-1] == -1:
                    human_6=analysis(i, j - 1, 1)
                    computer_6 = analysis(i,j-1,0)
                    chessboard[i][j-1]=-1
                    total_6 = max(human_6, computer_6)
                    value_p.append([i,j-1,total_6])
                #7方向
                if i+1 in range(15) and j-1 in range(15) and chessboard[i+1][j-1] == -1:
                    human_7=analysis(i + 1, j - 1, 1)
                    computer_7 = analysis(i+1,j-1,0)
                    chessboard[i+1][j-1]=-1
                    total_7 = max(human_7, computer_7)
                    value_p.append([i+1,j-1,total_7])
                #取部分综合排名最大值
                if value_p:
                    vmax=sorted(value_p,key=lambda x:x[2],reverse=True)
                    #print(vmax)
                    value.append(vmax[0])
                    #print(chessboard)

    if value:
        #取总体排名最大值
        vmax_total=sorted(value,key=lambda x:x[2],reverse=True)
        m = value[0][0]
        n = value[0][1]
        print(m,n)
        #保存白子
        chessboard[m][n]=0
        return m, n


while True:
    # 接受到退出指令后退出程序
    gomoku_exit()

    #放置棋盘
    screen.blit(chessboard_back, (0, 0))

    # 鼠标的坐标
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # 黑子跟随鼠标移动
    screen.blit(black, (mouse_x - 16, mouse_y - 16))

    # 获取鼠标的按键情况
    pressed_mouse = pygame.mouse.get_pressed()

    # 得到鼠标左键单击时的坐标
    if pressed_mouse[0]:
        pressed_x, pressed_y = pygame.mouse.get_pos()

        if logo == 0:
            tmp_x=pressed_x
            tmp_y=pressed_y
            logo=logo+1

            #显示鼠标单击后的坐标
            #print("(",pressed_x,",",pressed_y,")")

            #根据棋盘大小，计算白子棋盘坐标
            black_x_tmp=int((pressed_x-15)/52)
            black_y_tmp=int((pressed_y-15)/52)

            #判断坐标是否符合要求
            if black_x_tmp in range(0,15) and black_y_tmp in range(0,15):
                black_x.append(black_x_tmp)
                black_y.append(black_y_tmp)
                #print(black_x_tmp,black_y_tmp)
                chessboard[black_x_tmp][black_y_tmp]=1

                # 人机大战
                m,n=game()
                white_x.append(m)
                white_y.append(n)

                #清空black_x_tmp和black_y_tmp
                black_x_tmp=-1
                black_y_tmp=-1

        elif tmp_x != pressed_x and tmp_y != pressed_y :
            logo=0

    # 放置白子
    for i in range(len(white_x)):
        white_xx = white_x[i] * 52.5 + 15
        white_yy = white_y[i] * 52.5 + 15
        screen.blit(white, (white_xx, white_yy))

    if not black_x is None and not black_y is None:
        for i in range(len(black_x)):
            #计算黑子实际坐标
            black_xx=black_x[i]*52.5+15
            black_yy=black_y[i]*52.5+15
            #放置黑子
            screen.blit(black,(black_xx,black_yy))



    #判别失败函数
    for i in range(11):
        for j in range(11):
            #白棋胜
            if chessboard[i][j]==0:
                #横向五子连珠
                if chessboard[i+1][j]==0 and chessboard[i+2][j]==0 and chessboard[i+3][j]==0 and chessboard[i+4][j]==0:
                    ShowLoseScreen()
                #纵向五子连珠
                if chessboard[i][j+1]==0 and chessboard[i][j+2]==0 and chessboard[i][j+3]==0 and chessboard[i][j+4]==0:
                    ShowLoseScreen()
                #斜向上五子连珠
                if chessboard[i+1][j-1]==0 and chessboard[i+2][j-2]==0 and chessboard[i+3][j-3]==0 and chessboard[i+4][j-4]==0:
                    ShowLoseScreen()
                #斜向下五子连珠
                if chessboard[i+1][j+1]==0 and chessboard[i+2][j+2]==0 and chessboard[i+3][j+3]==0 and chessboard[i+4][j+4]==0:
                    ShowLoseScreen()

    #判别胜利函数
    for i in range(11):
        for j in range(11):
            # 黑棋胜
            if chessboard[i][j] == 1:
                # 横向五子连珠
                if chessboard[i + 1][j] == 1 and chessboard[i + 2][j] == 1 and chessboard[i + 3][j] == 1 and \
                                chessboard[i + 4][j] == 1:
                    ShowWinScreen()
                # 纵向五子连珠
                if chessboard[i][j + 1] == 1 and chessboard[i][j + 2] == 1 and chessboard[i][j + 3] == 1 and \
                                chessboard[i][j + 4] == 1:
                    ShowWinScreen()
                # 斜向上五子连珠
                if chessboard[i + 1][j - 1] == 1 and chessboard[i + 2][j - 2] == 1 and chessboard[i + 3][
                            j - 3] == 1 and chessboard[i + 4][j - 4] == 1:
                    ShowWinScreen()
                # 斜向下五子连珠
                if chessboard[i + 1][j + 1] == 1 and chessboard[i + 2][j + 2] == 1 and chessboard[i + 3][
                            j + 3] == 1 and chessboard[i + 4][j + 4] == 1:
                    ShowWinScreen()

    #刷新画面
pygame.display.update()
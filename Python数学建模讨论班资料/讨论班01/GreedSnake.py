# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 14:32:51 2021

@author: UMR
@read-me: 本程序没有在外观上下过多功夫，一方面为了节省时间，另一方面也避免喧宾夺主
键盘上下左右控制，q直接退出
在较高难度下，真实速度与电脑性能相关

拓展方向：添加墙，墙也可以动
改变规则：碰到边缘不是撞死而是传送到另一边
添加规则：限时大果，吃到增加3格长度
"""
import numpy as np
import time #休眠
import matplotlib.pyplot as plt
import funs #外置函数，使代码更清晰
import keyboard #检测键盘事件，控制上下左右 #pip install keyboard


#游戏设定
mapsize=20 #地图大小
level=10   #速度等级
winLength=25 #胜利长度
increaseLevel=True #开启难度递增
increaseSpeed=1.5  #难度增速

speed=1/level
       
#初始化
direct='w'
snakex=np.array([mapsize//2,mapsize//2+1])
snakey=np.array([mapsize//2]*2)
flag=0 #游戏状态 0=正常 1=失败 2=胜利 3=直接退出
lock=0 #锁定标记，确保一次move只允许改变一次方向
#snakex=snakex*sec

def callback(x):   #检测键盘事件，确定移动方向
    global direct
    global flag
    global lock
    if x.name=='up' and lock==0:
        if direct!='s' :
            direct='w' #防止直接回头撞死
            lock=1
    elif x.name=='left' and lock==0:
        if direct!='d' :
            direct='a'
            lock=1
    elif x.name=='down' and lock==0:
        if direct!='w' :
            direct='s'
            lock=1
    elif x.name=='right' and lock==0:
        if direct!='a' :
            direct='d'
            lock=1
    if x.name=='q':
        flag=3            
keyboard.on_press(callback) #其实是另开启了一个线程，与主程序画图互不干扰


plt.figure(figsize=(10,10),dpi=80,num="GREEDY snake") #确定画布大小，800*800
#figsize是长宽（英寸）dpi=每英寸像素数

fruitExist=1 #食物标记，1=存在，0=被吃，需要重新生成
p=funs.genFruit(snakex, snakey,mapsize) #生成食物（坐标）
while(True):
    if flag==3: #键盘终止（q键）
        break
    snakex,snakey,fruitExist=funs.updateSnake(snakex, snakey, direct, p) #更新蛇位置信息，并返回食物是否被吃掉
    lock=0 #解锁，现在到下一次更新位置，又可以进行一次变向
    flag=funs.checkWinOrLose(snakex, snakey,mapsize,winLength) #判定游戏状态：是否撞死，是否胜利
    if flag==1: #撞死
        print("gameover")
        break   
    plt.cla() #删除上一张画面，重新画图
    #在只有一张图（一个axes）时cla（清除当前axes）和clf（清除当前figure）等效
    funs.drawMap(np.size(snakex),winLength,speed) #画出地图边缘以及显示文字
    funs.drawSnake(snakex, snakey,mapsize) #画出蛇
    if not fruitExist: #如果食物被吃，就再生成一个
        p=funs.genFruit(snakex, snakey,mapsize)
        fruitExist=1
    funs.drawFruit(p, mapsize)  #画出食物
    plt.axis("equal") #设定x，y坐标轴单位长度相等
    plt.axis("off") #隐藏坐标轴
    if increaseLevel==True: #判断是否加速
        speed=1/(level+increaseSpeed*np.size(snakex))
    if flag==2: #判断是否胜利
        print("you win!!!")
        break
    plt.pause(speed) #定格（暂停）图像，不适用show()是因为show完就结束了
    time.sleep(speed) #同步暂停更新（暂停主线程），等待一定时间让玩家反应，但是仍可以识别键盘（多线程）
    
if flag==1: #游戏结束后，画出标语
    plt.text(0.3,0.5,"You Lost!",fontsize=80,fontweight='heavy',verticalalignment='center',color='r')

if flag==2:
    plt.text(0.3,0.5,"You WIN!!!",fontsize=80,fontweight='heavy',verticalalignment='center',color='gold')




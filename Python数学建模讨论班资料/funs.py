# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 09:30:56 2021

@author: UMR
"""



def drawMap(length,winLength,speed):
    import numpy as np
    import matplotlib.pyplot as plt
    edgex=np.array([0,0,1,1,0])#用惯matlab的同学，记得不要用空格分隔
    edgey=np.array([0,1,1,0,0])
    plt.plot(edgex,edgey,'dodgerblue',linewidth=5)
    plt.title('Length:'+str(length)+"   Goal:"+str(winLength)+"   Speed:"+str(1/speed*2//1/2),fontsize=20)
    
def drawSnake(x,y,mapsize):
    import matplotlib.pyplot as plt
    sec=1/mapsize
    plt.scatter(x*sec-sec/2,y*sec-sec/2,marker=',',s=400)
    #plt.scatter(x*sec-sec/2,y*sec-sec/2,marker=',',s=400,c=x*y*2+x+y,cmap="cool")
    
def genFruit(x,y,mapsize):
    import numpy as np
    
    p=np.ceil(np.random.rand(2)*mapsize)#推荐
    while checkColid(p, x, y):
        p=np.ceil(np.random.rand(2)*mapsize)
    return p

def drawFruit(p,mapsize):
    import matplotlib.pyplot as plt
    sec=1/mapsize
    plt.scatter(p[0]*sec-sec/2,p[1]*sec-sec/2,marker='.',s=2500,c="orange")
    
def checkColid(p,x,y):
    import numpy as np
    temp=x==p[0]
    temp=np.sum(y[temp]==p[1])
    return True if temp>0 else False#3目运算符

def moveSnake(x,y,direct):
    import numpy as np
    if direct=='w':
        x=np.insert(x,0,x[0])
        y=np.insert(y,0,y[0]+1)
    elif direct=='a':
        x=np.insert(x,0,x[0]-1)
        y=np.insert(y,0,y[0])
    elif direct=='s':
        x=np.insert(x,0,x[0])
        y=np.insert(y,0,y[0]-1)
    elif direct=='d':
        x=np.insert(x,0,x[0]+1)
        y=np.insert(y,0,y[0])
    return x,y       

def updateSnake(x,y,direct,p):
    import numpy as np
    x0,y0=moveSnake(x,y,direct)
    if checkColid(p,x0,y0):      
        return x0,y0,0
    x0=np.delete(x0,np.size(x0)-1)
    y0=np.delete(y0,np.size(y0)-1)
    return x0,y0,1

def checkWinOrLose(x,y,mapsize,winLength):
    import numpy as np    
    if x[0]<=0 or x[0]>mapsize:
        return 1
    elif y[0]<=0 or y[0]>mapsize:
        return 1   
    elif checkColid(np.array([x[0],y[0]]),np.delete(x,0),np.delete(y,0)):
        return 1
    elif np.size(x)>=winLength:
        return 2
    
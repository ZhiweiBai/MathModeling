# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 15:16:45 2021

@author: UMR
"""

import numpy as np
import time #休眠
import matplotlib.pyplot as plt
import keyboard #检测键盘事件，控制上下左右 #pip install keyboard

#只介绍常用的，其他的随用随查
#低频使用，不要追求全知全能

    #有些拼写并不是单词，注意
    #常用生成方式展示
a=np.array(([1,2],[2,3])) 
b1=np.arange(1,10,1)#起始，终止（不含），步长
b2=np.linspace(1,10,5)#起始，终止（含），总个数 
c=np.zeros((2,2))
d=np.ones((3,2),dtype="int")
e=np.eye(3)
f=np.empty((2,4))
g=np.random.rand(2,2)#有时候传一个元组，有时候传多个参数 
                #真随机，非正态分布，推荐 
                #0~1分布
                #多个参数来表示维度时，参数只能是维度，而用元组表示维度时，可以有其他参数（ep：dtye）
g1=np.ceil(np.random.rand()*5)#等可能生成1-5 #不要用round，思考原因
g2=np.floor(np.random.rand(2,2)*3)
g3=np.round(0.5)#3种取整
g4=np.round(1.5)#舍入遵循偶数原则，不用知道

    #常用特性展示 理解
h=np.array(([2,3],[1,3]))
h1=h*3#对每一个数*3
h2=h*h#对应位置的数相乘，因此要求形状相同
h3=np.dot(h,h)#内积
h4=h.dot(h)#内积
h5=np.sin(h)

h6=np.array((1,2))
h7=h6#直接等于没有经过计算，就是浅拷贝，相当于起小名，指向同一对象
h8=h6.copy()#深拷贝，互相独立
h6+=1#h7也+1了

    #常用属性读取展示 即用即查即可
i=np.size(d)#大小，=所有元素个数
it=d.size #另一种方式
i1=np.size(d,0)#生成时第一个参数大小，即“行数”
i2=np.size(d,1)#“列数”
i3=np.shape(d)
i4=d.dtype
i5=np.ndim(d)

    #常用操作展示
#变形
j=np.linspace(1,10,10)
j1=j.reshape(2,5)#不改变原数组，返回变形后数组
j2=np.linspace(1,6,6)
j_empty=j2.resize(3,2)#改变原数组，返回空
j3=np.resize(j,(5,2))#another写法
#增删改查
k=np.array([[1,3,2,4,5],[1,1,1,1,1]])#之后的操作都不会改变k
k1=np.append(k,99) #append会把数据拉成1维

k2=np.insert(k,3,99)#不指定第四个参数（axis）就先拉平，再插入
k3=np.insert(k,0,99,axis=0)#按行插入，若只有一个插入值，则改行全部等于此值
k4=np.insert(k,4,[99,66],axis=1)#按列插入，也可以直接指定插入的所有值，以元组或列表的形式

k5=np.delete(k,3)#一样，不指定axis就先拉平
k6=np.delete(k,1,0)#指定后，删掉一整行/一整列

ka=np.arange(1,10,1)
kb=np.linspace(-np.pi,np.pi,12).reshape(3,4)
ka1=ka[1:3]
ka2=ka[5:]
ka3=ka[:-3]
ka4=ka[1:10:2]#缺省第一，第二个参数，则默认选到一端结束，缺省第三个参数默认步长为1，步长可为负
ka5=ka[::-1]#反向
ka6=ka[[1,2,4,7]]#选出第2，3，5，8个数，注意：必须以列表的形式传参，否则会被理解成多维取数而报错

kb1=kb[1]#对多维数组，第一个参数是按行选取
kb2=kb[:,2]#这是按列
kb3=kb[1,2]#选出一个
kb4=kb[1:3,2:4]#选出一块，别忘了左闭右开

kc=np.linspace(-10,10,20).reshape(4,5)
kc1=kc[kc>3]
kc2=kc[kc*2>5]
kc3=kc/3<-1#直接给出bool矩阵，使用此矩阵可以直接取值，以及对其他形状相同的矩阵取值
kc4=kc[kc3]
kd=kc**2#乘方 matlab是^
kd1=kd[kc3]

    #次常用操作演示
la=np.arange(1,7,1).reshape(2,3)
lb=-la
l1=np.concatenate((la,lb),0)#axis=0:按行拼接
l2=np.concatenate((la,lb),axis=1)#1：按列
l3=np.concatenate((la,la,la,lb),1)#concatenate属实万能，可以同时拼接多个，只需记忆这一个即可

l4=np.split(la,3,1)#分谁，分几块，按行/列分 0=行 1=列
print(l4)




























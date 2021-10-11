```python
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 15:16:45 2021

@author: UMR
"""

import numpy as np
import time #休眠
import matplotlib.pyplot as plt#plot（）函数中的参数意思为：plot(x,y,形状)
import keyboard #检测键盘事件，控制上下左右 
#pip install keyboard
#应用实例：利用该代码可以实现录制 10 秒钟的键盘事件，并将其回放一遍
"""
import keyboard
import time

keyboard.start_recording()
time.sleep(10)
events = keyboard.stop_recording()
keyboard.replay(events)
"""

#只介绍常用的，其他的随用随查
#低频使用，不要追求全知全能
#有些拼写并不是单词，注意
#常用生成方式展示
#此处的内容是方便大家理解整个逻辑，不太明白也不太会影响使用的。NumPy 数组的维数称为秩（rank），秩就是轴的数量，即数组的维度，一维数组的秩为 1，二维数组的秩为 2，以此类推。
#在 NumPy中，每一个线性的数组称为是一个轴（axis），也就是维度（dimensions）。比如说，二维数组相当于是两个一维数组，其中第一个一维数组中每个元素又是一个一维数组。所以一维数组就是 NumPy 中的轴（axis），第一个轴相当于是底层数组，第二个轴是底层数组里的数组。而轴的数量——秩，就是数组的维数。
#很多时候可以声明 axis。axis=0，表示沿着第 0 轴进行操作，即对每一列进行操作；axis=1，表示沿着第1轴进行操作，即对每一行进行操作。

a=np.array(([1,2],[2,3])) #array：数组。 array() 函数可以将 Python 的任何序列类型转换为 ndarray 数组。
b1=np.arange(1,10,1)#()内参数的含义为：【起始，终止（不含）），步长

#range and np.range的区别
#range()和np.arange()的返回类型不同，range()返回的是range；object，而np.arange()返回的是ndarray类型range()不支持步长为小数，而np.arange()支持步长(step)为小数range()和np.arange()都可用于迭代；range()和np.arange()都有三个参数，以第一个参数为起点，第三个参数为步长，截止到第二个参数之前的不包括第二个参数的数据序列。range()可用于迭代，而np.arange作用远不止于此，它是一个序列，可被当做向量使用。
   
    
b2=np.linspace(1,10,5)#创建形式为等差序列的一维数组的函数，参数意义分别是：起始，终止（含），总个数 
c=np.zeros((2,2))#0矩阵
d=np.ones((3,2),dtype="int")#单位矩阵
e=np.eye(3)#对角矩阵
f=np.empty((2,4))#创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组
g=np.random.rand(2,2)#生成一个服从【0,1）均匀分布的随机样本值
                     #有时候传一个元组，有时候传多个参数 
                     #真随机，非正态分布，推荐 
                     #0~1分布不包括1
                     #多个参数来表示维度时，参数只能是维度，而用元组表示维度时，可以有其他参数（ep：dtye）
                     #还有np.random.seed 用于科研结果的复现 

g1=np.ceil(np.random.rand()*5)#向上取整
                              #等可能生成1-5 
                              #不要用round，思考原因,随机数范围【0~1）#向上取整
g2=np.floor(np.random.rand(2,2)*3)#向下取整
g3=np.round(0.5)#该句语法为np.round(x,[,n])x 是数值表达式，n 是数值表达式，表示从小数点位数。作用是返回浮点数x的四舍五入值。当参数n不存在时，round()函数的输出为整数。当参数n存在时，即使为0，round()函数的输出也会是一个浮点数。此外，n的值可以是负数，表示在整数位部分四舍五入，但结果仍是浮点数。
g4=np.round(1.5)#舍入遵循偶数原则，例如2.5会变成2，3，5会变成3

    
    
#常用特性展示 理解
h=np.array(([2,3],[1,3]))
h1=h*3#对每一个数*3
h2=h*h#对应位置的数相乘，因此要求形状相同，不是矩阵乘，而是点乘
h3=np.dot(h,h)#内积
h4=h.dot(h)#内积
h5=np.sin(h)#对矩阵内每一个数都应用这个函数

h6=np.array((1,2))
h7=h6#直接等于没有经过计算，就是浅拷贝，相当于起小名，指向同一对象，可以联系指针来理解
h8=h6.copy()#也可表示为np.copy(h6)
            #深拷贝，互相独立
h6+=1#在浅拷贝时h7也+1了，但在深拷贝则不会


#常用属性读取展示 即用即查即可
i=np.size(d)#大小，=所有元素个数
it=d.size #另一种方式查看数组元素的总个数
i1=np.size(d,0)#生成时第一个参数大小，即“行数”
i2=np.size(d,1)#“列数”
i3=np.shape(d)#数组的维度
i4=d.dtype#class下既有属性也有函数，了解类的知识
i5=np.ndim(d)#dim是英文dimension维度的缩写，因此对于一个数组，其shape属性的长度（length）也既是它的ndim.


#常用操作展示
#变形
j=np.linspace(1,10,10)#生成等差数列
j1=j.reshape(2,5)#不改变原数组，返回变形后数组，-1的用法，但必须要能够整除
j2=np.linspace(1,6,6)
j_empty=j2.resize(3,2)#改变原数组，返回空
j3=np.resize(j,(5,2))#another写法


#增删改查
k=
k=np.array([[1,3,2,4,5],[1,1,1,1,1]])#之后的操作都不会改变k
k1=np.append(k,99) #append会把数据拉成1维

k2=np.insert(k,3,99)
#用法是将向量插入某一行或列，语法为：numpy.insert(arr, obj, values, axis=None)
#不指定第四个参数（axis）就先拉平，再插入,如果是多维只插入一个数，那就会先拉平再插
#如果是三维变二维呢？一个数就利用广播机制拉平，但如果是3需要2则不可以，会报错

k3=np.insert(k,0,99,axis=0)#按行插入，若只有一个插入值，则改行全部等于此值，广播机制
k4=np.insert(k,4,[99,66],axis=1)#按列插入，也可以直接指定插入的所有值，以元组或列表的形式

k5=np.delete(k,3)#一样，不指定axis就先拉平，k是原来的，返回了一个不同的东西
k6=np.delete(k,1,0)#指定后，删掉一整行/一整列

#ka是一维，kb是多维
ka=np.arange(1,10,1)
kb=np.linspace(-np.pi,np.pi,12).reshape(3,4)
ka1=ka[1:3]
ka2=ka[5:]
ka3=ka[:-3]
ka4=ka[1:10:2]#缺省第一，第二个参数，则默认选到一端结束，缺省第三个参数默认步长为1，步长可为负，左闭右开，后面是步长
ka5=ka[::-1]#反向
ka6=ka[[1,2,4,7]]#选出第2，3，5，8个数，注意：必须以列表的形式传参，否则会被理解成多维取数而报错

kb1=kb[1]#对多维数组，第一个参数是按行选取
kb2=kb[:,2]#这是按列选取
kb3=kb[1,2]#选出一个特定的数组
kb4=kb[1:3,2:4]#选出一块区域内包含的数组，别忘了左闭右开

kc=np.linspace(-10,10,20).reshape(4,5)
kc1=kc[kc>3]
kc2=kc[kc*2>5]
kc3=kc/3<-1#直接给出bool矩阵，使用此矩阵可以直接取值，以及对其他形状相同的矩阵取值
kc4=kc[kc3]
kd=kc**2#**表示乘方 matlab是^
kd1=kd[kc3]

    #次常用操作演示
la=np.arange(1,7,1).reshape(2,3)
lb=-la
l1=np.concatenate((la,lb),0)#函数在一个指定的轴上连接多个数组。它接受一个数组序列作为参数，并将它们连接成一数组。 
                            # axis=0:按行拼接，=1则按列拼接
                            #其标准语法为：numpy.concatenate((a1, a2,...),axis= 0, out= None) 
l2=np.concatenate((la,lb),axis=1)#1：按列
l3=np.concatenate((la,la,la,lb),1)#concatenate属实万能，可以同时拼接多个，只需记忆这一个即可

l4=np.split(la,3,1)#其标准语法为：np.split(ary,indices_or_sections, axis=0)
#作用是把一个数组从左到右按顺序切分
print(l4)
#不均等分割的语法



























```


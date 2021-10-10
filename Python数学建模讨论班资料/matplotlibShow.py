# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 09:06:10 2021

@author: UMR
"""

import numpy as np 
import matplotlib.pyplot as plt

#一共分4级，figure，axes，axis，trick，常用前三个
#figure=整张图表、显示的一切、画板
#axes=一张完整的图，一个figure可以画任意张图
#axis=一张图的坐标与网格
#trick=刻度
a=np.random.rand(50)
b=plt.figure()#缺省原则，自动plt.figure(1)
c=plt.subplot(121)#缺省，自动plt.subplot(111)
#一行，两列，第一个位置
#如果只画了一张图，就算定义了多行多列，还是只会显示一张，因为显示区域只显示有内容的部分
#直接subplot默认给上一个figure添加
#subplot是一种便捷地生成axes地方式，否则需要手动指定axes的顶点坐标
print(b.axes)
b.add_subplot(122)#也可以显式地指定给目标添加axes
print(b.axes)

#当只有一个figure时，其实可以全部缺省
#使用gcf() gca()获取当前对象
figure=plt.gcf() #get current figure
axes=plt.gca() #get current axes
axes.plot(a)

fig = plt.figure()  #定义新的三维坐标轴，默认figure 2了
ax3 = plt.axes(projection='3d')#3D画图模式

#定义三维数据
x = np.arange(-5,5,0.5)
y = np.arange(-5,5,0.5)
X, Y = np.meshgrid(x, y)#便捷拉网，相当于生成了一个网，将网每个点的x，y坐标储存在X，Y中
Z = np.sin(X)+np.cos(Y)


#作图
ax3.plot_surface(X,Y,Z,cmap='rainbow')#需要什么功能就现查吧
ax3.contour(X,Y,Z,offset=-2,cmap='rainbow')   #等高线图，要设置offset，为Z的最小值
plt.show()#show了，这张figue就不改了，所以最后show

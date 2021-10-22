### 2.数据处理与可视化

#### 2.1数值计算工具NumPy

##### 2.1.1数组的创建，属性和操作

​       通过NumPy库的array函数实现数组的创建，如果向array函数中传入了一个列表或元组，将构造简单的一维数组；如果传入多个嵌套的列表或元组，则可以构造一个二维数组。构成数组的元素都具有相同的数据类型。下面分别构造一维数组和二维数组。

```python
利用array函数创建数组示例。
#程序文件Pex2_1.py
import numpy as np    #导入模块并命名为np
a = np.array([2,4,8,20,16,30])  #单个列表创建一维数组
#嵌套元组创建二维数组
b = np.array(((1,2,3,4,5),(6,7,8,9,10),
              (10,9,1,2,3),(4,5,6,8,9.0)))
print("一维数组：",a)
print("二维数组：\n",b)

执行结果：
一维数组： [ 2  4  8  20  16  30]
二维数组：
 [[ 1.  2.  3.  4.  5.]
 [ 6.  7.  8.  9. 10.]
 [10.  9.  1.  2.  3.]
 [ 4.  5.  6.  8.  9.]]

```

##### 2.1.2数组的属性查看

```python

print("维数：",a.ndim);   #维数：2
print("维度：",a.shape)       #维度：（3,5）
print("元素总数：",a.size);    #元素总数：15
print("类型：",a.dtype)       #类型：int32
print("每个元素字节数：",a.itemsize)  #字节数：4

```

##### 2.1.3数组元素的索引

​       NumPy比一般的Python **序列提供更多的索引方式。除了用整数和切片的一般索引外，数组还可以布尔索引及花式索引。**

①对于一维数组来说，Python原生的列表和NumPy的数组的切片操作都是相同的，无非是记住一个规则：列表名（或数组名）[start: end: step]*，但不包括索引end对应的值。

②二维数据列表元素的引用方式为a[i][j]；array数组元素的引用方式为a[i,j]。

```Python
import numpy as np
a = np.array([2,4,8,20,16,30])  
b = np.array(((1,2,3,4,5),(6,7,8,9,10),
              (10,9,1,2,3),(4,5,6,8,9.0)))
print(a[[2,3,5]])  #一维数组索引，输出：[ 8 20 30]
print(a[[-1,-2,-3]])   #一维数组索引，输出：[30 16 20]
print(b[1,2])  #输出第2行第3列元素：8.0
print(b[2])    #输出第3行元素：[10.  9.  1.  2.  3.]
print(b[2,:])  #输出第3行元素：[10.  9.  1.  2.  3.]
print(b[:,1])  #输出第2列所有元素：[2.  7.  9.  5.]
print(b[[2,3],1:4])  #输出第3、4行，第2、3、4列的元素
print(b[1:3,1:3])    #输出第2、3行，第2、3列的元素

```

##### 2.1.4数组的修改，变形

```Python
#注意reshape和resize的区别
#通常是使用resize改变数组的尺寸大小，使用reshape用来增加数组的维度。
```

##### 2.1.5数组的运算，通用函数与广播运算

NumPy 算术函数包含简单的加减乘除: **add()**，**subtract()**，**multiply()** 和 **divide()**。

需要注意的是数组必须具有相同的形状或符合数组广播规则。

#### 2.2文件操作

```Python
#read
#关闭文件
# if “ae" in line 正则表达式，如何找出，find，count函数
#先w后r
#绝对路径和相对路径
例2.26  向文本文件写入数据示例。
#程序文件Pex2_26.py
f1=open("Pdata2_26.txt","w")
str1=['Hello',' ','World!']; str2=['Hello','World!']
f1.writelines(str1); f1.write('\n')
f1.writelines(str2); f1.close()
f2=open('Pdata2_26.txt')
a=f2.read(); print(a)

运行结果：
Hello World!
HelloWorld!



import numpy as np
a = []; b = []; c = []#引入了三个列表
with open('Pdata2_21.txt') as file:#用with open不用担心关没关，用open如果下面报错影响到close
    for (i, line) in enumerate(file):
        elements = line.strip().split()#strip ()，s为字符串，rm为要删除的字符序列。智能删除开头或是结尾的字符或是字符串，不能删除中间的字符或字符串。
        if i < 6:
            a.append(list(map(float, elements[:8])))#利用map函数将元素从0到7取浮点数，
            b.append(float(elements[-1].rstrip('kg')))
        else:
            c = [float(x) for x in elements]
a = np.array(a); b = np.array(b); c = np.array(c)
print(a,'\n',b,'\n',c)

#enumerate是枚举的意思，返回对象的每个元素都是一个元组，每个元组包括两个值，一个是计数，一个是sequence的值，计数是从start开始的，start默认为0。

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))       # 小标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
#为什么用那么多迭代器
 #目的是为了在编写算法尽可能使用要求最低的迭代器，并让它适用于容器的最大区间。 
    
#列表推导式：它的结构是在一个中括号里包含一个表达式，然后是一个for语句，然后是 0 个或多个 for 或者 if 语句。那个表达式可以是任意的，意思是你可以在列表中放入任意类型的对象。返回结果将是一个新的列表，在这个以 if 和 for 语句为上下文的表达式运行完成之后产生。列表推导式的执行顺序：各语句之间是嵌套关系，左边第二个语句是最外层，依次往右进一层，左边第一条语句是最后一层。
[x*y for x in range(1,5) if x > 2 for y in range(1,4) if y < 3]
#执行顺序：
for x in range(1,5)
    if x > 2
        for y in range(1,4)
            if y < 3
                x*y
 #列表没有办法运算，列表和元组没有shape属性，它的大小是元素的个数，数组有形状shape,有shape属性，可以通过array.shape获取数组的形状大小shape。列表并不为数组产生。            
                
                
```

##### 2.2.3文件管理方法

​      Python的os模块提供了类似于操作系统级的文件管理功能，如显示当前目录下的文件和目录列表、文件重命名、文件删除、目录管理等。要使用这个模块，需要先导入它，然后调用相关的方法。

```python
import os
a=os.listdir("c:\\")      
print(a)     #显示C根目录下的文件和目录列表
print("-------------------------------------")
b=os.listdir(".")         
print(b)     #显示当前工作目录下的文件和目录列表
#excel读取所以用pandas
#np.sin和math.sin
#数据框可以直接做点乘吗，可以把values取出来做
```

```python
#程序文件Pex2_36.py
import numpy as np, pandas as pd
from matplotlib.pyplot import *
a=pd.read_excel("Pdata2_33.xlsx",usecols=range(1,4))  #提取第2列到第4列的数据
c=np.sum(a)  #求每一列的和
ind=np.array([1,2,3]); width=0.2
rc('font',size=16); bar(ind,c,width); ylabel("消费数据")
xticks(ind,['用户A','用户B','用户C'],rotation=20)  #旋转20度
rcParams['font.sans-serif']=['SimHei']   #用来正常显示中文标签
savefig('figure2_36.png',dpi=500)   #保存图片为文件figure2_36.png，像素为500

#rc改变了所有，一般用来改变不能显示的中文或者符号

```

#### 2.3数据处理工具Pandas

Pandas中必须要了解的内容有序列，数据帧，重索引等

```python
#pandas封装在numpy之上，主要作为数据分析工具

import pandas as pd
import numpy as np
import math


##文件读取与数据
df2=pd.read_csv('./data1.csv')   #读取csv数据
# 也有read_excel等
print(df2.head())  #可以读取默认前5条数据，括号内值可以指定读取数量
  Unnamed: 0  a  b  c  d  e   f
0          A  1  1  2  3  4   5
1          B  2  2  3  4  5   6
2          C  3  3  4  5  6  dm
3          D  4  4  5  6  7   8
4          E  5  5  6  7  8   9
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 7 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   Unnamed: 0  5 non-null      object
 1   a           5 non-null      int64 
 2   b           5 non-null      int64 
 3   c           5 non-null      int64 
 4   d           5 non-null      int64 
 5   e           5 non-null      int64 
 6   f           5 non-null      object
dtypes: int64(5), object(2)
memory usage: 408.0+ bytes
df2.info()   #可以返回当前的信息

print(df2.index)   #调取索引
print(df2.columns)   #调取列名
RangeIndex(start=0, stop=5, step=1)
Index(['Unnamed: 0', 'a', 'b', 'c', 'd', 'e', 'f'], dtype='object')
30
print(df2.dtypes)   #dtypes值
print(df2.values)   #调取数值
Unnamed: 0    object
a              int64
b              int64
c              int64
d              int64
e              int64
f             object
dtype: object
[['A' 1 1 2 3 4 '5']
 ['B' 2 2 3 4 5 '6']
 ['C' 3 3 4 5 6 'dm']
 ['D' 4 4 5 6 7 '8']
 ['E' 5 5 6 7 8 '9']]

#Series和DataFrame
a=pd.Series(data=[1,2,3],index=["i","love","u"])
print(a[2])
print(a["love"])

b=np.arange(1,7).reshape(3,2)
df=pd.DataFrame(b,index=['a','b','c'],columns=['x1','x2'])#直接建立
print(df)
   x1  x2
a   1   2
b   3   4
c   5   6

da={'data1':['a','b','c','d'],'data2':[1,2,3,4],'data3':['alpha','beta','gamma','zeta']}
df_da=pd.DataFrame (da)  #字典和DataFrame的转换
print(df_da)
  data1  data2  data3
0     a      1  alpha
1     b      2   beta
2     c      3  gamma
3     d      4   zeta

da_2=df_da ['data2']
print(da_2)
print(da_2[1:2])
0    1
1    2
2    3
3    4
Name: data2, dtype: int64
1    2
Name: data2, dtype: int64

##索引
print(df_da[['data1','data2']])   #可以同时找出多列的数据，注意要把列名作为整体来索引
  data1  data2
0     a      1
1     b      2
2     c      3
3     d      4
#loc按照label索引
#iloc按照position索引
# print(df_da[0])
print(df_da.iloc[0])
print(df_da.iloc[0:2])
print(df_da.iloc[0:2,0:2])#切片
da_1=df_da.set_index('data1')     #可以不用编号索引，可用DataFrame里面的一列作为索引
print(da_1)
# print(da_1['data1'])     #此时已经没有data1这一列
print(da_1['data2'])   #会出现自己指定的索引
print(da_1['data2']['b'])
# print(da_1['b']['data2'])  #直接索引是取不了行的
#上面为普通索引，先取列，再取行；下面为loc通过位置索引，先取行再取列  还有哪些区别？
# 取出一个值的方式
print(da_1.loc['b','data2'])
print(da_1.iloc[1,0])

print(da_1.loc['a':'c','data2':'data3'])  #与上面取切片相同，不过‘：’可以取到最后一位

print(da_1[da_1['data2']>2])   #bool类型的索引
print(da_1[da_1['data2']==1]['data2'].mean())

##运算
df_da['data2']+=10  #加减
print(df_da['data2'])
da1=pd.Series(data=[1,1,1,1,1],index=['a','b','c','d','e']);
da2=pd.Series(data=[1,1,1,1,1],index=['c','d','e','f','g']);
print(da1+da2);  #会按照当前索引进行加减操作
0    11
1    12
2    13
3    14
Name: data2, dtype: int64
a    NaN
b    NaN
c    2.0
d    2.0
e    2.0
f    NaN
g    NaN
dtype: float64
df_da['data2']*=10   #乘除
print(df_da['data2'] )
print(df_da['data2'].mean())  #平均值
print(df_da['data2'].max())   #最大值

# print(math.sin(df_da['data2']))   #？
print(list(map(math.sin,df_da['data2'])))   #map前要加list


print(df_da.describe())  #直接给出统计数据，但是只有数值的列统计
[0.8414709848078965, 0.9092974268256817, 0.1411200080598672, -0.7568024953079282]
          data2
count  4.000000
mean   2.500000
std    1.290994
min    1.000000
25%    1.750000
50%    2.500000
75%    3.250000
max    4.000000

##groupby
dff={'key':['A','B','C','A','B','C','A','B','C'],'data1':[1,2,3,4,5,6,6,6,6],'data2':[100,110,120,130,140,150,160,170,180]}
df3=pd.DataFrame(dff)
print(df3)

  key  data1  data2
0   A      1    100
1   B      2    110
2   C      3    120
3   A      4    130
4   B      5    140
5   C      6    150
6   A      6    160
7   B      6    170
8   C      6    180
    data1                                              data2               \
    count      mean       std  min  25%  50%  75%  max count   mean   std   
key                                                                         
A     3.0  3.666667  2.516611  1.0  2.5  4.0  5.0  6.0   3.0  130.0  30.0   
B     3.0  4.333333  2.081666  2.0  3.5  5.0  5.5  6.0   3.0  140.0  30.0   
C     3.0  5.000000  1.732051  3.0  4.5  6.0  6.0  6.0   3.0  150.0  30.0   

                                        
       min    25%    50%    75%    max  
key                                     
A    100.0  115.0  130.0  145.0  160.0  
B    110.0  125.0  140.0  155.0  170.0  
C    120.0  135.0  150.0  165.0  180.0  
key
A    390
B    420
C    450
Name: data2, dtype: int64
      data2                                                     
      count   mean        std    min    25%    50%    75%    max
data1                                                           
1       1.0  100.0        NaN  100.0  100.0  100.0  100.0  100.0
2       1.0  110.0        NaN  110.0  110.0  110.0  110.0  110.0
3       1.0  120.0        NaN  120.0  120.0  120.0  120.0  120.0
4       1.0  130.0        NaN  130.0  130.0  130.0  130.0  130.0
5       1.0  140.0        NaN  140.0  140.0  140.0  140.0  140.0
6       4.0  165.0  12.909944  150.0  157.5  165.0  172.5  180.0
print(df3.groupby('key').describe())
print(df3.groupby('key')['data2'].sum())
print(df3.groupby('data1').describe())

```



#### 2.4Matplotlib可视化

在Matplotlib库中提供了两种风格的API供开发者使用。这也就是为什么有人用`plt.xx`，有人用`ax.xx`的原因。好的代码应该坚持使用一种风格，否则会显得混乱，阅读起来困难，不利于维护。此处推荐使用面向对象的编程接口。

让我们先来了解图标各部分的名称：

坐标轴(axis)

坐标轴名称(axis label)

坐标轴刻度(tick)

坐标轴刻度标签(tick label)

坐标轴边界（lim）

网格线(grid)

图例(legend)

标题(title)

边框（spine）

##### 2.4.1导入Matplotlib

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
```

##### 2.4.2绘图

```python
#设置标题
ax.set_title('标题',fontdict={'size':16},loc = 'left')    #设置16px的字体大小，将标题显示在左侧

#设置边框
ax.spines['right'].set_visible(False)   #去除右边的spines
ax.spines['bottom'].set_color('r')  #设置底部的spines为红色

#设置坐标轴
ax.set_xlabel('季度',fontsize=16)
ax.set_xlabel('销售额',fontsize=16)
# 更改刻度标签。此例将0，1，2，3更改为一季度，二季度，三季度，四季度
ax.set_xticks(ind)
ax.set_xticklabels(quarter)

# 设置刻度标签属性
# axis : 可选{‘x’, ‘y’, ‘both’} ，选择对哪个轴操作，默认是’both’
# labelsize设置刻度标签的大小
# direction{‘in’, ‘out’, ‘inout’}刻度线的方向
# color : 刻度线的颜色
# labelcolor : 刻度值颜色
ax.tick_params(axis = 'y', labelsize=14,direction='in',labelcolor='r')

#设置刻度间隔
#从pyplot导入MultipleLocator类，这个类用于设置刻度间隔
from matplotlib.pyplot import MultipleLocator
#把x轴的刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(1)
#把y轴的刻度间隔设置为10，并存在变量里
y_major_locator=MultipleLocator(10)
#把x轴的主刻度设置为1的倍数
ax.xaxis.set_major_locator(x_major_locator)
#把y轴的主刻度设置为10的倍数
ax.yaxis.set_major_locator(y_major_locator)

#设置边界
ax.set_xlim([0,12])  # x轴边界
ax.set_ylim([0,50])  # y轴边界
```

利用plt.show()进行绘制

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()
#除此之外我们还可以使用%matplotlib notebook将产生嵌入在笔记本中的交互式绘图，%matplotlib inline将产生嵌入在笔记本中的绘图的静态图像
#易错点要先保存再show
```

##### 2.4.3将图形保存到文件

```python
fig.savefig('my_figure.png')
```

应用：在绘画时的自定义

```python
# 使用灰色背景
ax = plt.axes(axisbg='#E6E6E6')
ax.set_axisbelow(True)

# 绘制白色实网格线draw solid white grid lines
plt.grid(color='w', linestyle='solid')

# 隐藏轴的刻度
for spine in ax.spines.values():
    spine.set_visible(False)

# 隐藏顶部和右侧刻度
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()

# 将刻度和标签变亮
ax.tick_params(colors='gray', direction='out')
for tick in ax.get_xticklabels():
    tick.set_color('gray')
for tick in ax.get_yticklabels():
    tick.set_color('gray')

# 控制直方图的人脸和边界颜色
ax.hist(x, edgecolor='#E6E6E6', color='#EE6666');
```


#pandas封装在numpy之上，主要作为数据分析工具

import pandas as pd
import numpy as np
import math

##文件读取与数据
df2=pd.read_csv('./data1.csv')   #读取csv数据
#也有read_excel等
#print(df2.head())  #可以读取默认前5条数据，括号内值可以指定读取数量
#df2.info()   #可以返回当前的信息
#print(df2.index)   #调取索引
#print(df2.columns)   #调取列名
#print(df2.dtypes)   #dtypes值
#print(df2.values)   #调取数值


##Series和DataFrame
a=pd.Series(data=[1,2,3],index=["i","love","u"])
#print(a[2])
#print(a["love"])

b=np.arange(1,7).reshape(3,2)
df=pd.DataFrame(b,index=['a','b','c'],columns=['x1','x2'])#直接建立
print(df)

da={'data1':['a','b','c','d'],'data2':[1,2,3,4],'data3':['alpha','beta','gamma','zeta']}
df_da=pd.DataFrame (da)  #字典和DataFrame的转换
#print(df_da)
da_2=df_da ['data2']
#print(da_2)
#print(da_2[1:2])


##索引
#print(df_da[['data1','data2']])   #可以同时找出多列的数据，注意要把列名作为整体来索引

#loc按照label索引
#iloc按照position索引
#print(df_da[0])
#print(df_da.iloc[0])
#print(df_da.iloc[0:2])
#print(df_da.iloc[0:2,0:2])#切片

da_1=df_da.set_index('data1')     #可以不用编号索引，可用DataFrame里面的一列作为索引
#print(da_1)
#print(da_1['data1'])     #此时已经没有data1这一列
#print(da_1['data2'])   #会出现自己指定的索引
#print(da_1['data2']['b'])
#print(da_1['b']['data2'])
#上面为普通索引，先取列，再取行；下面为loc通过位置索引，先取行再取列  还有哪些区别？
# 取出一个值的方式
# print(da_1.loc['b','data2'])
# print(da_1.iloc[1,0])

# print(da_1.loc['a':'c','data2':'data3'])  #与上面取切片相同，不过‘：’可以取到最后一位

# print(da_1[da_1['data2']>2])   #bool类型的索引
# print(da_1[da_1['data2']==1]['data2'].mean())


##运算
df_da['data2']+=10  #加减
#print(df_da['data2'])
da1=pd.Series(data=[1,1,1,1,1],index=['a','b','c','d','e']);
da2=pd.Series(data=[1,1,1,1,1],index=['c','d','e','f','g']);
#print(da1+da2);  #会按照当前索引进行加减操作

df_da['data2']*=10   #乘除
#print(df_da['data2'] )
#print(df_da['data2'].mean())  #平均值
#print(df_da['data2'].max())   #最大值
#print(math.sin(df_da['data2']))   #？
# print(list(map(math.sin,df_da['data2'])))   #map前要加list


#print(df_da.describe())  #直接给出统计数据，但是只有数值的列统计

##groupby
dff={'key':['A','B','C','A','B','C','A','B','C'],'data1':[1,2,3,4,5,6,6,6,6],'data2':[100,110,120,130,140,150,160,170,180]}
df3=pd.DataFrame(dff)
# print(df3)
# print(df3.groupby('key').describe())
# print(df3.groupby('key')['data2'].sum())
print(df3.groupby('data1').describe())
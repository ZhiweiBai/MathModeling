# Python 在高数和线代中的应用——总结文档

## 1 背景

SymPy 是 Python 版的开源计算机代数系统实现，通俗地讲 SymPy 是 用于符号运算的工具库。SymPy 包括许多功能，从基本的符号算术到多项式、微积分、求解方 程、离散数学和统计等。它主要处理三种类型的数据：整型数据、实数和有 理数。有理数包括两个部分：分子和分母，可以用 Ration 类定义有理数。 本节通过示例程序来理解 SymPy 的概念及应用。

## 2 实例

### 2.1 求极限


$$
\lim_{x\rightarrow 0}\frac{\sin x}{x}, \lim_{x\rightarrow +\infin}(1+\frac{1}{x})^x
$$

```python
from sympy import *
x=symbols('x')
print(limit(sin(x)/x,x,0))
print(limit(pow(1+1/x,x),x,oo)) #这里是两个小”o”，表示正无穷
```

### 2.2 求导数

$$
z=\sin x+x^{2} e^{y}, \text { 求 } \frac{\partial^{2} z}{\partial x^{2}}, \frac{\partial z}{\partial y}
$$

```python
from sympy import *
x,y=symbols('x y') # 定义两个符号变量
z=sin(x)+x**2*exp(y) # 构造符号表达式
print("关于 x 的二阶偏导数为：",diff(z,x,2))
print("关于 y 的一阶偏导数为：",diff(z,y))
```

### 2.3 级数求和

$$
\text { 验证 } \sum_{k=1}^{n} k^{2}=\frac{n(n+1)(2 n+1)}{6}, \sum_{k=1}^{\infty} \frac{1}{k^{2}}=\frac{\pi^{2}}{6} \text { 。 }
$$

```python
from sympy import *
k,n=symbols('k n')
print(summation(k**2,(k,1,n)))
print(factor(summation(k**2,(k,1,n)))) # 把计算结果因式分解
print(summation(1/k**2,(k,1,oo))) # 这里是两个小 o 表示正无穷
```

### 2.4 泰勒展开

写出 $\sin x$ 在 0 点处的 $3,5,7$ 阶泰勒展开式, 并在同一图形界面 上画出 $\sin x$ 及它的上述各阶泰勒展开式在区间 $[0,2]$ 上的图形。

```python
from pylab import rc
from sympy import *
rc('font',size=16); rc('text',usetex=True)
x=symbols('x'); 
y=sin(x)
for k in range(3,8,2): 
    print(y.series(x,0,k)) # 等价于 print(series(y,x,0,k))
plot(y,series(y,x,0,3).removeO(),series(y,x,0,5).removeO(),
 	series(y,x,0,7).removeO(),(x,0,2),xlabel='$x$',ylabel='$y$')
```

```
x + O(x**3)
x - x**3/6 + O(x**5)
x - x**3/6 + x**5/120 + O(x**7)
```

![image-20210920161018200](https://gitee.com/bai299/images/raw/master/image-20210920161018200.png)


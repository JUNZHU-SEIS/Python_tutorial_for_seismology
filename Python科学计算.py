# %% [markdown]
# # Pandas处理表数据
# 以美国USGS下载的地震目录为例，用pandas筛选出目录中5级以上，深度100km以下的地震

# %%
import pandas as pd
ctlg = pd.read_csv('data/usgs_catalog_20230300_0330.csv')
#print(ctlg)
#print(df.describe())
subctlg = ctlg[((ctlg.mag>5)&(ctlg.depth>100))]
print(subctlg.describe())
subctlg.plot.scatter(x='longitude',y='latitude')

# %% [markdown]
# # Numpy代替for循环，做向量和矩阵运算
# * 一维数组
#   * 向量算数运算
#   * 通用函数
#   * 向量逻辑运算
# * 二维数组
#   * 广播机制
# * 线性代数
# * I/O

# %%
import numpy as np
# 一维数组
## 构造均匀分布的浮点数数组
x0 = np.linspace(0,1,11)
x1 = np.arange(11)/10
## 构造全1/0数组
x2 = np.ones(11)
x3 = np.zeros(11)
## 以函数形式构造数组sin(x)，其中x为[0,pi]区间的10等分点
x4 = np.cos(x0*np.pi)
## 拼接两个数组x0,x4
x5 = np.hstack([x0,x4])
print(x0,x1,x2,x3,x4,x5)

# %%
# 向量算术运算
## 向量与常数
x0+1 # x0*2;x0/2;x0**2
## 向量与向量
x0+x1 #x0-x1;x0*x1;x0/(x1+1e-10);np.dot(x0,np.array([[0],[1]]))

# %%
# 通用函数
print(np.sign.__doc__)
#abs;angle;real;imag;conj;fix
#cos;sin;tan;arccos;arcsin;arctan;arctan2;cosh;sinh;tanh;arccosh;arcsinh;arctanh
#exp;log;log10;sqrt
#mean;min;max;std;sum;var;correlate;cumsum;prod;cumprod
#poly

# %%
# 向量逻辑运算
logic = np.zeros_like(x0)
index = x0>.5#筛选出x0内大于.5的数
logic[index] = 1
print(x0,index,logic)

# %%
# 二维数组
## 构造二维数组
xy0 = np.array([[0,1,2,3],[4,5,6,7]])
print(xy0,xy0.shape)
## 访问其中某个元素
print(xy0[1,1])
## 切片
print(xy0[1:,:-1])
## 改造数组形状
print(np.reshape(xy0,(4,-1)))
## 转置
print(xy0.T)
## 构造单位矩阵，对角矩阵
print(np.identity(3))

# %%
## 广播（当两个一维数组的维度不一样时，依然可以做算数运算）
x1T = np.expand_dims(x1,axis=1)
z = x1T+x2 #x1T*x2;x1T/(x2+1e-10)
print(x1T)
print(z,x1+x2)

# %%
# 线性代数
## 矩阵乘法
A = np.matrix([[1,2],[3,4]])
b = np.matrix([[5],[6]])
C = A*b
print(C)
## 求解线性方程组
import numpy.linalg as npl
x = npl.solve(A,b)
print(x)

# %%
# I/O (深度学习领域最喜欢的I/O方式)
np.savez('test.npz',data=x0)
d = np.load('data/test.npz')
print(d['data'])
## 其他I/O方式：loadtxt

# %% [markdown]
# # Scipy做科学计算

# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp

duration = 1.0
fs = 400.0
samples = int(fs*duration)
t = np.arange(samples)/fs
# We create a chirp of which the frequency increases from 20 Hz to 100 Hz and apply an amplitude modulation.
signal = chirp(t, 20.0, t[-1], 100.0)
signal *= (1.0+0.5*np.sin(2.0*np.pi*4.0*t)) #可以改变调幅信号的周期观察波形的变化

analytic_signal = hilbert(signal)
amplitude_envelope = np.abs(analytic_signal)

# %% [markdown]
# # Maplotlib可视化

# %%
plt.plot(t, signal, label='signal')
plt.plot(t, amplitude_envelope, label='envelope')
plt.xlabel("Time (s)")
plt.legend()
plt.tight_layout()
plt.savefig('hilbert.pdf')

# %% [markdown]
# # 推荐阅读
# * 《Python科学计算》 作者：John M. Stewart
# * https://pandas.pydata.org/docs/user_guide/index.html#user-guide
# * https://numpy.org/doc/stable/user/index.html#user
# * https://docs.scipy.org/doc//scipy/tutorial/index.html#user-guide
# * https://matplotlib.org/stable/tutorials/index.html
# * 关于Python画地图，请参考 https://www.pygmt.org/latest/index.html



# %% [markdown]
# # 为什么学Python?
# Python 是一种广泛使用的通用编程语言，其具有**语法简单、 功能强大、方便维护、免费开源**等优点，是目前地震学科研最常用的编程语言之一。越来越多的地震学软件使用Python语言，如：
# * Obspy (天然地震学领域用来下数据，处理波形的库)
# * SeisGlitch (火震去除毛刺)
# * SeisBench (地震学领域训练机器学习模型及获取公开数据集的多功能平台)
# * PhaseNet (用于地震震相拾取的机器学习模型)
# * EQTransformer (同PhaseNet)
# * Seispy (接收函数)
# * PyGMT (Python版的GMT，地理绘图工具)
# * PALM (一套全流程地震定位工具)

# %% [markdown]
# # Python变量和简单数据类型
# * 字符串
# * 整数/浮点数
# * 列表
# * 元组
# * 字典

# %%
import math
# 注意遵守变量命名规范（数字不打头，不空格，不用关键字，简短且具描述性，慎用字母IO）
# 字符串
message = "Hello, world"
print(message)
print(message+'\nenter\ttab')
# 整数/浮点数
i = 25
print(i,i+1,i**2,i//3,i%3,math.sqrt(i))
# 列表（存储可变数据）
list = [1,2,'a','b',.1]
print('列表：',list,'列表长度：',len(list))
list[0] = '被修改的元素'
list.append('添加的元素')
print('访问列表元素/切片：',list[0],list[-2],list[:-1])
print('列表生成式：',[x**2 for x in range(10)])
# 元组（存储不可变数据）
tuple = (1,2,'a','b',.1) #与列表的区别是用括号声明
#tuple[1] = 3
print('元组：',tuple)
# 字典（键-值对）
dic = {"学生A":{"姓名":"A","学号":'PB20XXXXX','学期成绩':[100,100,100,100]}}
print(dic)
print(dic['学生A']['姓名'])
print(dic.keys(),dic.values())

# %% [markdown]
# # Python函数和类
# * 一个度转千米的函数
# * 创建一个描述汽车的类，要求该类可以更新汽车里程
# * 创建一个描述地震事件的类

# %%
def deg2km(dist,radius=6371):
    # 注意缩进
    return dist*math.pi/180*radius
print('1度约为%.2f km'%deg2km(1))

class Car(): #类命名一般大写
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odo_meter = 0
        self.unit = 'm'
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name
    def read_meter(self):
        return '当前里程是%d %s'%(self.odo_meter,self.unit)
    def update_odometer(self,increment):
        self.odo_meter += increment

car = Car('audi','a4',2016)
print(car.get_descriptive_name())
print(car.read_meter())
car.update_odometer(100)
print(car.read_meter())

# 创建一个描述地震事件的类，要求该类可以计算事件到任何台站的距离
class Event():
    def __init__(self,time,x,y,depth,mag):
        self.time = time
        self.depth = depth
        self.mag = mag
        self.x = x
        self.y = y
    def dist2station(self,x,y,elevation=0):
        dh = math.sqrt((self.x-x)**2+(self.y-y)**2)
        dz = abs(self.depth+elevation/1e3)
        return math.sqrt(dh**2+dz**2)

# 创建一个事件
event = Event('20230330000000',0,0,12,5)
# 求该事件到一个台站的距离
print(event.dist2station(3,4))

# %% [markdown]
# # Python I/O
# 以美国USGS网站发布的地震目录文件为例，读取并存储其前5列信息，并将分隔符改成一个空格

# %%
with open('data/usgs_catalog_20230300_0330.csv','r') as f:
    lines = f.readlines()
out = open('trimed_catalog.txt','w')
for line in lines:
    #抽取前5列信息
    saved = ' '.join(line.split(',')[:6])+'\n'
    out.write(saved)
out.close()

# %% [markdown]
# # 推荐阅读
# 蟒蛇书：《Python编程 从入门到实践》前11章
# 
# ![](data/python.jpg)



#!/usr/bin/env python
# coding: utf-8

# # 读取 Excel 文件

# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```

# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ```

# ## 默认读取
# 
# 
# 默认读取是最简单的方式，使用 `pd.read_csv('xxxx.csv')` 即可读取对应文件
# 
# 现在尝试使用 `pandas` 读取当前目录下 `某招聘网站数据.csv`
# 

# In[1]:


import pandas as pd
data = pd.read_csv("某招聘网站数据.csv")


# ```{admonition} 注意
# :class: Attention
# 
# 使用 `pandas` 读取 `CSV` 与读取 `xlsx` 格式的 `Excel` 文件方法大致相同
# 
# 因此下面与 `Excel` 相关的读取操作均以 `CSV` 格式进行介绍
# 
# ```

# ## 读取前 n 行
# 
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件的 **前20行**

# In[2]:


data = pd.read_csv("某招聘网站数据.csv",nrows = 20)


# ## 跳过前 n 行
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件并 **跳过前20行**

# In[3]:


data = pd.read_csv("某招聘网站数据.csv",skiprows = [i for i in range(1,21)])


# ## 指定行读取
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件中全部**偶数行**

# In[4]:


data = pd.read_csv('某招聘网站数据.csv', skiprows=lambda x: (x != 0) and not x % 2)


# ```{admonition} 思考
# :class: hint
# 
# 如果是读取全部奇数行，或者更多满足指定条件的行呢？
# ```

# In[5]:


data = pd.read_csv('某招聘网站数据.csv', skiprows=lambda x: x % 2) #读取奇数行


# ## 指定列号读取
# 
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件的第 `1、3、5` 列

# In[6]:


data = pd.read_csv("某招聘网站数据.csv",usecols = [0,2,4])


# ##  指定列名读取
# 
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件的 `positionId、positionName、salary` 列

# In[7]:


data = pd.read_csv("某招聘网站数据.csv",usecols = ['positionId','positionName','salary'])


# ## 指定列匹配读取
# 
# 
# 让我们来个更难一点的，还是读取 `某招聘网站数据.csv` 文件，但现在有一个 list 中包含多个字段👇
# 
# `usecols = ['positionId','test','positionName', 'test1','salary']`
# 
# 如果 `usecols` 中的列名存在于 `某招聘网站数据.csv` 中，则读取。

# In[8]:


usecols = ['positionId', 'test', 'positionName', 'test1', 'salary']

data = pd.read_csv('某招聘网站数据.csv', usecols=lambda c: c in set(usecols))


# ## 读取时设置索引
# 
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件，并在读取时将 `positionId` 设置为索引列

# In[9]:


data = pd.read_csv('某招聘网站数据.csv',index_col=['positionId'])


# ## 读取时设置标题
# 
# <br>
# 
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件的 `positionId、positionName、salary` 列，并将标题设置为 `ID、岗位名称、薪资`

# In[10]:


data = pd.read_csv('某招聘网站数据.csv', usecols=[0,1,17],header = 0,names=['ID','岗位名称','薪资'])


# ## 读取并处理缺失值
# 
# 
# 
# 
# - 读取当前目录下 `某招聘网站数据.csv` 文件，**并不将缺失值标记为 `NA`**
# - 读取当前目录下 `某招聘网站数据.csv` 文件，**并将`[]`标记为缺失值**
# - 读取当前目录下 `某招聘网站数据.csv` 文件，**但不处理缺失值**

# In[11]:


data = pd.read_csv('某招聘网站数据.csv', keep_default_na=False)

data = pd.read_csv('某招聘网站数据.csv',na_values=['[]'])

data = pd.read_csv("某招聘网站数据.csv",na_filter=False)


# ```{admonition} 思考
# :class: hint
# 
# 这三种方式有什么区别？
# ```

# ## 读取时设置格式
# 
# 
# - 读取当前目录下 `某招聘网站数据.csv` 文件，并将 `positionId,companyId` 设置为字符串格式
# 
# - 读取当前目录下 `某招聘网站数据.csv` 文件，并将 `createTime` 列设置为时间

# In[12]:


data = pd.read_csv("某招聘网站数据.csv", dtype={'positionId': str,'companyId':str}) #指定字符串格式

data = pd.read_csv("某招聘网站数据.csv",parse_dates=['createTime']) #指定时间格式


# ## 分块读取
# 
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件，要求返回一个可迭代对象，每次读取 10 行

# In[13]:


data = pd.read_csv("某招聘网站数据.csv", chunksize= 10)


# ```{admonition} 思考
# :class: hint
# 
# 为什么这样做？
# ```

# ## 循环读取数据
# 
# 
# 在 `demodata` 文件夹下有多个 `Excel` 文件，要求一次性循环读取全部文件

# In[14]:


import os
path = 'demodata/'
filesnames = os.listdir(path)
filesnames = [f for f in filesnames if f.lower().endswith(".xlsx")]
df_list = []
for filename in filesnames:
    df_list.append(pd.read_excel(path + filename))

df = pd.concat(df_list)


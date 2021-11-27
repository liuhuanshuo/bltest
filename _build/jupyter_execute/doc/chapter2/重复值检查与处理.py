#!/usr/bin/env python
# coding: utf-8

# # 重复值检查与处理

# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```

# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ```

# In[1]:


import pandas as pd
df = pd.read_excel("TOP250.xlsx")
pd.set_option('display.max_colwidth',10)


# ## 查找全部重复值
# 
# 
# 将全部缺失值所在的行筛选出来

# In[2]:


df[df.duplicated()]


# ## 查找指定列重复值
# 
# 上面是所有列完全重复的情况，但有时我们只需要根据某列查找缺失值
# 
# -> 查找 片名 列全部缺失值

# In[3]:


df[df.duplicated(['片名'])]


# ## 删除全部重复值
# 
# 删除全部的重复值

# In[4]:


df = df.drop_duplicates()


# ## 保留重复值
# 
# 删除全部的重复值，但保留最后一次出现的值

# In[5]:


df = df.drop_duplicates(keep = 'last')


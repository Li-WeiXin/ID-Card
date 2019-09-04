import pickle
import os
import re

# 将txt文件生成列表
with open('./3755.txt','r') as f:
    line = f.read().strip()
    result = re.split(r"[\s\n]", line)
    # print(result)

# 生成字典
text = {}
text = dict(zip(range(3755), result))
print(text)

with open('chinese_labels','wb')as f:
    i = pickle.dump(text,f,0)

print(i)



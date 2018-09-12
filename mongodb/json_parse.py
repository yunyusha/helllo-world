import json
import os
# 读取文件中的数据
file = open('infor.json', 'r', encoding='utf-8')
data = file.read()
# print(isinstance(data, str))
file.close()
"""
json: 前端和后台约定的一种数据传输格式,由数组和字典组合得到的字符串结构

json解析: 将json字符串解析成当前语言可以识别的数据结构
"""
data = json.loads(data)
print(data)
for item in data:
    for img in item['photo']:
        print(img)
file.close()
# json归档: 将由列表和字典组合得到的数据转换成一个json类型的字符串


dict1 = {'name': 'xiaocai', 'score': (10, 20, 30, 40)}
str1 = json.dumps(dict1)
print(str1)
f = open('json1.json', 'w')
f.write(str1)
f.close()


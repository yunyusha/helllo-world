# def circle(n):
#     for i in range(n):
#         print('你当前返回的是数字{0}'.format(i))
#         yield i
#
# result = circle(10)
# # print(result)
# print(next(result))
# print(next(result))

"""
yield和return作用类似,都能够完成对函数结果的返回,但是不同之处是yield返回的生成器
生成器每一次生成结果都会控制函数对应内容的回调,此种方式可以提高程序的执行效率
"""
import re
a = "ff1213fd"
x = re.findall("\d+",a)
print(x)

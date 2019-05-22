import json
# jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
# test = json.loads(jsonData)
# print(test['a'])
b = {1:2}
c = {2:3}
d = {**b,**c}
a = [{1:2},{1:3}]
print(a[1][1])
for i in range(2):
    a[i][1+3] = a[i][1]


print(d)
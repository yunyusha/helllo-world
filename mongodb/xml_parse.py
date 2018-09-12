from xml.etree import ElementTree as ET
# 读取文档数据
# tree = ET.parse('Person.xml')
# 获取xml文档数据的根元素(最外层元素)
# root = tree.getroot()
# for el in root:
#     for ell in el:
#         print(ell)

# 在ET解析中每一个标签都会解析成Element对象,每一个
# Element对象内部都具有一下几种方法:
"""
find(tag/xpath):通过指定的标签名或xpath路径查找对应
Element对象中指定的一个子集元素

findall(tag/xpath):通过指定的标签名或xpath路径查找对应
Element对象中指定的所有子集元素

findtext(tag/xpath): 通过指定的标签名或xpath路径查
找对应Element对象中指定的一个子集元素的文本内容

text: Element对象的属性,用来设置或者获取对应Element对象
标记的文本内容

iter(tag): 将整个xml结构每一个标签全部合并转换成一个独立的生成器对象,
如果指定tag,此时生成器中只包含tag指定的标签.

"""
# res = [item.text for item in root.findall('Person/name')]

# res = root.iter('name')
# for item in res:
#     print(item.text)

# Element中存在的属性操作
# res = root.iter('Person')
# for per in res:
#     per.set('data', '傻B')
#     print(per.get('data'))

# 生成xml数据
# Element对象的DOM操作
"""
ET.Element(name): 创建一个普通的Element对象
ET.SubElement(parent, name): 创建一个子级Element对象
"""
# 定义函数用来完成Element创建和组装
def create_combine(parent, childName, text=None, attr=None, value=None):
    # 创建对应的子集Element
    child = ET.SubElement(parent, childName)
    # 设置子集元素标记的文本内容
    if text is not None:
        child.text = text
    # 在子级元素末尾添加换行
    child.tail = '\n'
    # 设置子级元素的属性
    if attr is not None:
        child.set(attr, value)
    # 将子集元素插入到父级元素

# 开始组装
# 创建根元素
root = ET.Element('xml')
create_combine(root, 'user', '小菜')
create_combine(root, 'pass', 'xssxs')
create_combine(root, 'time', '2018-07-19')
# 将xml数据转换成ElementTree对象
# tree = ET.ElementTree(root)
# tree.write('note.xml', encoding='utf-8', xml_declaration=True)

# 将root结构转换成字符串
xml_str = ET.tostring(root)
print(xml_str)

# xml解析


root2 = tree.getroot()
usr = next(root2.iter('user')).text()
pass1 = next(root2.iter('pass')).text()
time_str = next(root2.iter('time')).text()
print(usr+":"+pass1+":"+time_str)




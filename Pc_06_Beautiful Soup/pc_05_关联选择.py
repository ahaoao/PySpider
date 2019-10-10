from bs4 import BeautifulSoup
import requests


url = 'http://www.baidu.com'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')

# （1）.子节点和子孙节点：直接子节点调用 contents属性，调用children属性得到相应的结果。
# print(soup.p.contents)  # 返回列表
# print(soup.p.children)  # 返回结果是生成器类型，需要用for来读取
# print(soup.p.descendants)  # 返回结果是生成器类型
# for i, child in enumerate(soup.p.children):
#     print(i, child)
# descendants 会递归查询所有子节点，得到所有子孙节点
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)

# （2）.父节点和祖先节点
# 获取某个节点的父节点：parent  ,这里输出的仅仅是a节点的直接父节点，而没有再向外寻找父节点的祖先节点
# print(soup.a.parent)
# # 获取a所有的祖先节点，可以调用parents
# print(soup.a.parents)  # 返回结果是生成器
# print(type(soup.a.parents))
# print(list(enumerate(soup.a.parents)))
# for i, child in enumerate(soup.a.parents):
#     print(i, child)

# （3）.兄弟节点：
# # next_sibling: 获取节点的下一个兄弟元素
# # prevous_sibling: 获取节点的上一个兄弟元素
# # next_siblings: 返回后面的兄弟节点
# # prevous_siblings: 返回前面的兄弟节点
# print('Next Sibling', soup.link.next_sibling)
# print('Prev Sibling', soup.link.previous_sibling)
# print('Next Siblings', list(enumerate(soup.link.next_siblings)))
# print('Prev Siblings', list(enumerate(soup.link.previous_siblings)))


# 提取信息
print('Next Sibling:')
print(type(soup.link.next_sibling))
print(soup.link.next_sibling)
print(soup.link.next_sibling.string)
print('Parent:')
print(type(soup.div.parents))
# print(list(enumerate(soup.div.parents)))
print(list(soup.div.parents)[0])
print(list(soup.div.parents)[0].attrs)
print(list(soup.div.parents)[0].attrs['link'])

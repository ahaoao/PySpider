list1 = [1,2,3,4]
list2 = [5,6,7,8]
# 同时遍历两个列表用zip函数
for (i1, i2) in zip(list1, list2):
    Dict = {
        'name': i1,
        'value': i2
    }
    print(Dict)

import pymongo

# 第一个参数地址，第二个端口为参数
Client = pymongo.MongoClient(host='localhost', port=27017)
# 指定数据库  test   等价方式：db = Client['test']
db = Client.test
# 指定集合（相当于关系数据库的表）student， 等价方式：collection = db['student']
collection = db.students
# 集合student以字典的形式表示
student = {
    'id': '201810411221',
    'name': 'ahao',
    'age': '21',
    'gender': 'male'
}
# 调用collection的insert()方法插入数据
result = collection.insert(student)
print(result)

# Python3.X 中使用insert_one()和insert_many()方法来分别插入单条和多条记录
student0 = {
    'id': '201810411220',
    'name': 'ah',
    'age': '20',
    'gender': 'male'
}
result1 = collection.insert_one(student0)
print(result1)
print(result1.inserted_id)

# insert_many()数据以列表的形式传递, 调用inserted_ids
student1 = {
    'id': '201810411222',
    'name': 'h',
    'age': '20',
    'gender': 'ma'
}
student2 = {
    'id': '201810411228',
    'name': 'h',
    'age': '10',
    'gender': 'me'
}
student3 = {
    'id': '201810411229',
    'name': 'wwh',
    'age': '25',
    'gender': 'le'
}
result2 = collection.insert_many([student1, student2, student3])
print(result2)
print(result2.inserted_ids)

# 查询 利用find_one()和 find()方法进行查询，其中find_one()得到的是单个结果，find()返回的是一个生成器对象,需要遍历取结果
result3 = collection.find_one({'name': 'ahao'})
print(type(result3))
print(result3)

result4 = collection.find({'gender': 'male'})
# result4 返回结果是Cursor类型，需要遍历取所有结果，其中每个都是字典。
print(result4)
for result in result4:
    print(result)

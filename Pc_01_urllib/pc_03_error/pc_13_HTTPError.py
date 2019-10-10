from urllib import request, error
#
try:
    response = request.urlopen('http://cuiqingcai.com/index.htm')
    print(response.read().decode('utf-8'))
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')

# 以上代码最好写法为以下代码
# URLError 是 HTTPError的父类，先选择捕获子类的错误信息，再去捕获父类的错误
"""
以下代码做到：先捕获HTTPError 获取它的错误状态代码，原因，headers 等信息。
如果不是HTTPError 则会捕获URLError 异常，输出错误原因，最后用else来处理正常的逻辑
"""
try:
    response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='/n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')
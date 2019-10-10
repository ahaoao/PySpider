import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\s(\w+)\s(\w\w)', content)
print(result)
print(result.group())
print(result.group(1))  # 对应正则表达式第一个() 即(\d+) 
print(result.group(2))  # 对应正则表达式第二个() 即(\w+)
print(result.group(3))  # 对应正则表达式第三个() 即(\w\w)
print(result.span())
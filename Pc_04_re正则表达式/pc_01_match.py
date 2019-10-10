import re

# match() 方法是从字符串的开头开始匹配的，一旦开头不匹配，那么整个匹配就失败了
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}', content)  # 匹配的长度只能小于等于目标字符串长度，大于目标字符串长度会报错
print(result)
print(result.group())  # group()方法可以输出匹配到的内容

print(result.span())  # span()方法可以输匹配的范围

"""
正则表达式： ^Hello\s\d\d\d\s\d{4}\s\w{10} ^是用来匹配字符串开头Hello，然后\s匹配空白字符，匹配空格，
\d{3}表示3个 \d 来匹配123 ， \d{4}表示用4个 \d 来匹配4567 ，\w{10}用来匹配10个字母及下划线 
"""

import re

"""
万能匹配表达式  ： .* （点星） .(点)可以匹配任意字符(除换行符), *(星)代表匹配前面的字符无限次.
"""
content = 'Hello 123 4567 World_This is Regex Demo'
result = re.match('^Hello.*Demo$', content)  # $是结尾字符串
print(result)
print(result.group())
print(result.span())
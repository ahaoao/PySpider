import re

content = """Hello 1234567 World_This
is a Regex Demo
"""
result = re.match('^H.*?(\d+).*?Demo$', content, re.S)  # re.S修饰符可以使 . 匹配包括换行符在内的所有字符
print(result.group(1))
import re


# search 匹配时会扫描整个字符串，然后返回第一个匹配成功的结果。也就是说正则表达式可以说字符串的一部分。
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)
print(result.group(1))
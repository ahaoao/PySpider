import re

"""
贪婪匹配：.*会匹配尽可能多的字符，正则表达式中.*后面是\d+ ，也就是至少一个数字，并没有指定具体多少个数字。
因此.*尽可能匹配多的字符，这里把123456匹配了，给\d+留下一个可能满足条件的数字7，最后得到的内容就只有数字7
非贪婪匹配： .*? 相对于贪婪匹配多了一个? , 非贪婪匹配尽可能匹配少的字符，当.*? 匹配到Hello后面的空白字符时，
再往后的字符就是数字了，而\d+恰好可以匹配到，那么这里的.*?就不再进行匹配，交给\d+ 去匹配后面的数字。

"""

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'http://jianshu.com/search?q=python&page=1&type=collections'))

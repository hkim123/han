import re

P = re.compile('(a(b)c)d')
m = P.match('abcd')
print (m.group(0))  # 전체 match 된 pattern 을 나타낸다.
print (m.group(1))  # 첫번째 괄호 안에 있는 pattern 을 나타낸다.
print (m.group(2))  # 두번째 괄호 안에 있는 pattern 을 나타낸다.
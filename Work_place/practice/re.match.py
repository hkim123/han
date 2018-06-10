import re

list = ["guru99 get", "guru give", "guru99 Selenium"]

for element in list:
    z = re.match("(g\w+)\W(g\w+)",element)  # g 로 시작하는 글자 와 다음글자 또한 g 로 시작하는 글자를 찾는 함수, /W 는 with 의 의미.
    if z:
        print((z.group()))  #print(z) doesn't work, 반드시 group 을 사용해야 함

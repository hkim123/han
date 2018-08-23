a = 'a,b,c,' \
    'i am han kim'

b = a.split('\n')  #split('\n')은 enter 에 따라 짤라서 list 형태로 저장한다.

print b



lines = 'Very good morning Jacob Abraham.\n How are you doing today!'
for item in lines: #글짜(알파벳 하나하나로 구분
    print (item)   #알파벳 하나하나 print include space

for item in lines.splitlines():   ## enter 를 기점으로 분류
    print (item.strip())  # 공백을 없애줌.
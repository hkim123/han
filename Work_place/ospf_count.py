import re

output = 'Count: 18 lines'
#match = re.search('Count: ([0-9]+) lines', output)
match = re.search('Count: (\d+) lines', output)   #this is same meaning of above. \d means number
neighbor = 18
#print(match)
print(match.group(0))
print(match.group(1))
print(match.group(2))   # 만약 group(2)를 만들고 싶으면 () 를 하나 더 만들어야 됨. 여기서는 (lines)라고 하면 됨
#print re.findall('\\d+', output)



if match:
    if (int(match.group(1)) != int(neighbor)):
        print('fail')
    else:
        print('pass')


#match1 = re.match(r"(\w+) (\w+)", "Han Kim")
#print (match1)
#print (match1.group(0))
#print (match1.group(1))
#print (match1.group(2))

#family = ('han kim, heesuk lee')
#match2 = re.search('han kim', family)
#print (match2)
#print (match2.group(0))
#print (match2.group(1))



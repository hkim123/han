import re
xx = "guru10 education is fun"

r1 = re.findall(r"^\w+",xx)
print((re.split(r"\s", 'we are spliting the words')))
print((re.split(r"s",'wesare spliting the words')))  # if found s, makes s as space. example wesare ---> we are,  words ----> word and space

print(r1)

#r2 = re.split(r"\s+",xx)
#print(r2)

#print((re.split(r's','we are splitting the words')))
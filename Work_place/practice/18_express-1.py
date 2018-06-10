import re
pattern = "aza"
str1 = "azaa1103bbb"

match1=re.match(pattern, str1)
print (match1)
print (match1.group())
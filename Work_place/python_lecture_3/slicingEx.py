#슬라이스에 name 설정

aa = [1,2,5,11,3,6,7,10]
saa = aa[3:6]

record  = "김말동2419911123서울시"
code ="2011 2014 2015 1999 1981"
birth_year = slice(5,9)
print(record[birth_year])
name = slice(0,3,2) #index 0 부터 3 까지
print(record[name])

scode = slice(0,24)
print(code[scode])
scode = slice(0,10,2) #2는 스텝ㅇ다.
print(code[scode])

#indices(len)

record1 = "고길동1501012341234서울"
print(name.indices(len(record1)))
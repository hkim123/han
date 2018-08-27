#unpacking (반드시 요소의 갯수와 변수의 갯수가 일치하여야 한다)
'''
pa = (1,2)

a,b = pa  #위 pa 튜플의 각각의 요소를 a,b 에 assign 함

print(a)
print(b)

li_data = ["홍길동", 23, "서울",(1980, 11, 21)]
name, age, local, birthday = li_data
print(name)
print(age)
print(local)
print(birthday)

#위의 list 에서 튜플을 다시 하나하나 빼고 싶을때.
name, age, local, (year, month, day) = li_data
print(year)
print(month)
print(day)

#문자열도 가능하다
str = "Hello"
a,b,c,d,e = str

print(a)

a,b,*c = str
print(c)


#특정값을 무시하거나 *를 이용해서 여러개를 언패킹하기
name, _, local, _ = li_data  #age 와 birthday 는 무시

print(name)
print(local)

##### * 사용 예  ##############
person_info = ("장길산","hkk@jki.com","010-123-1234","02-567-1234")
name, email, *phone = person_info   #전화번호 2개다 출력된다.

print(name)
print(email)
print(phone)


pointValue = [10, 5, 12, 11, 22, 14, 12, 15, 10, 10, 15, 14, 15]
*prePoint, curPoint = pointValue   # *preValue 앞에 * 이 있어니, 마지막 하나까지의 요소를 뜻한다.

print(prePoint)
print(curPoint)

'''

###############################################################
address = [("우",234, 123), ("도","서울"),("도","경기"),("우",123,234)]

def show_zipcode(num1,num2) :
    print("우",num1, num2)

def show_local(str):
    print("도",str)

for key, *arg in address:
    if key == "우" :
        show_zipcode(*arg)
    elif key == "도":
        show_local(*arg)


###################   무자열 에서도 가능 ###############
str2 = "홍길동/23/12345465/9876543/010-123-2345/서울"
name, age,*num, local = str2.split("/")
print(name)
print(age)
print(local)

################ *_ 를 사용하면 필요한 data만 가지고 올수 있다 #############
li_data = ["홍길동", 23, "서울",(1980, 11, 21)]
name, *_,(year,*_) = li_data
print(name)
print(year)


# coding=utf-8
import socket
host=socket.gethostbyname_ex("www.google.com")
print "\n ---------- Host print -----------"
print host

# for 문을 이용해 값을 한 줄씩 출력

print "\n -------------- Print Host info each line -------------"

for i in host :
    print i

# 값에서 마지막 데이타가 IP 목록 이므로 그중 첫번째 주소를 IP 로 선택

(hostname, aliaslist, ipaddrlist) = host

print "\n ----------- ip address choosed ------------"
print "ip :", ipaddrlist[0]



# enumerate 샤용법을 우심히 볼것,
mytuple = ("a","b","c")
for item in mytuple :
    print "data =", item


for index, item in enumerate(mytuple) :
    print "인덱스 = ", index , ", 데이타 = ", mytuple[index]
    print index,mytuple[index]

# enumerate 샤용법을 우심히 볼것,my_list[c] 이지 my_list(index) 가 아님.
my_list = (7,8,9)
for c, index in enumerate(my_list) :
     print (c, index)
     print c, my_list[c]

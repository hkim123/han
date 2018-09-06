#dictionary 에서 최소값/최대값/정렬
#dictionary 는 key 와 value 값으로 구분되어진다, 정렬은 value 값을 가지고 정렬한다.

fruits = {
    "사과": 300,
    "오렌지":500,
    "바나나":500,
    "배":1000,
    "포도":2000
}

#zip 함수를 이용해서 key 와 값을 뒤집는다.
max_fruits = max(zip(fruits.values(),fruits.keys())) #해당값을 뒤집어서 최대값을 구한다.
print(max_fruits)

min_fruits=(min(zip(fruits.values(),fruits.keys())))
print(min_fruits)

sorted_fruits = sorted(zip(fruits.values(),fruits.keys()))
print(sorted_fruits)

#zip 은 한번만 사용가능하다
fruits_name = zip(fruits.values(),fruits.keys())
print(max(fruits_name))
#print(min(fruits_name))   #### 이경우 error 발생, min 을 구하려면 zip 을 한번 더 사용해야 된다

####key 값을 가지고 비교 하는 경우, key 를 비교하여 최소 key 를 리턴한다.
print(min(fruits))  ### 바나나 가 "ㅂ" 이므로 제일 먼저 나온다.
print(max(fruits))

#### value 값만 가지고 하는 경우
print(max(fruits.values()))  ### 2000 이 나온다
print(min(fruits.values()))  ### 300 이 나온다.

###zip 을 사용하지 않고 키와 값을 동시에 얻는 경우
print(min(fruits, key = lambda n: fruits[n])) #min 의 key 함수를 적용한 예
print(max(fruits, key = lambda n: fruits[n]))

### 최대값과 일치하는 key 를 얻어오고자 할
max_val = max(fruits, key = lambda n:fruits[n])
print(max_val)

#### 같은 값을 가지고 비교하는 경우, 이 경우는 key 값만 가지고 비교한다, 즉 사과의 "ㅅ"이 "ㅇ" 보다 먼저
fruits1 = {"사과":300,"오렌지":300}
print(min(zip(fruits1.values(),fruits1.keys())))



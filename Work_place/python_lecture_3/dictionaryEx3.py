#두개의 dictionary 에서 동일값,동일 키를 얻어오기

x = {
    "a":100,
    "b":200,
    "c":300
}

y = {
    "c":300,
    "d":200,
    "a":150
}

#### 동일한 Key 값 구하기 ###
xy = x.keys() & y.keys()
print(xy)

#### key 값 빼기
x_y = x.keys() - y.keys()
print(x_y)

# key 와 value 이 동일한 아이템을 찾기

xy_key_val = x.items() & y.items()
print(xy_key_val)

#### value 만 구하기 ####
xy_val = x.values()
print(xy_val)

#### 특정 key 값을 뺀 새로운 딕셔너리를 만들때

z = {key:x[key] for key in x.keys()- {"b","c"}}  ### b 와 c 를 뺀다
print(z)

z = {key:y[key] for key in y.keys() - {"b","c"}} ### b 와 c 를 빼는데, b 가 없기 때문에 c 만 뺀다
print(z)
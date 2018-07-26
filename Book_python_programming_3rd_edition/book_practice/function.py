# Function

def print_fun():
    print ("This is function code ")

print_fun()  # this is call the function
print_fun()  # you can use an many you want

#This is exchange function (Korean won exchage to US dollar)
def kor_usd(kor):
    dollar = kor // 1000

    print ("$",dollar)

kor_usd (1000) # Korean 1,000 exchange to USD Dollar
kor_usd (9000) # Korean 9,000 exchange to USD Dollar

# return value : this is not print out immediately and save to variable and use it
def allow_dating_age(my_age):
    girls_age = my_age // 2
    return girls_age

dating_limit = allow_dating_age(50) # this actual value save to valiable dating_limit
print("dating age will be" , dating_limit, "or old" )


### variable scope
'''
this case a is outside of function so it can use both corn and fuzy
but if a is inside of function, only that function can use that variable
'''

a= 1234
def corn():
    print(a)

def fuzy():
    a=4321 # if this a is not here, it will print out 1234
    print(a)

corn()
fuzy()


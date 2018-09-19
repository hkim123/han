## Question1 ##

print("####Question 1####")
Cel = input("Enter a degree in Celsius : ")

Fah = (9/5)*eval(Cel) + 32

print(Cel + " Celsinus is" , Fah,"Fahrenheit" )

## Question2 ##

print("####Question 2####")
InvestAmount = eval(input("Enter investment amount: "))
Month_Rate = eval(input("Enter annual interest rate : ")) / 1200
number_month = eval(input("Enter number of years: ")) * 12

Future_Value = int(InvestAmount * (1 + Month_Rate) ** number_month *100) / 100

print("Accumulated value is ", Future_Value)

##Questin 3 ##

print("####Question 3####")
num = eval(input("Enter a number between 0 and 1000 : "))

num_1 = num % 10
temp_1 = num // 10

num_2 = temp_1 % 10
temp_2 = temp_1 // 10

num_3 = temp_2 % 10
num_4 = temp_2 // 10

sum = num_1 + num_2 + num_3 + num_4

print("The sum of the digit is ", sum)


##Questin 4 ##

print("####Question 4####")

weight_kilo = eval(input("Enter weight in pound: ")) * 0.45359237
height_meter = eval(input("Enter height in inches : ")) * 0.0254

BMI = round(weight_kilo / height_meter ** 2, 4)

print("BMI is", BMI)

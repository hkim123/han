'''
## Question 1 ###

#a = int(input("Enter an ASII code: "))
#chr_1 = chr(a)
#print("The character is " + chr_1)

##Question 2 ##
print(format(57.467657,"9.3f"))
print(format(12345678.923,"9.1e"))
print(format(5789.4,"<.2f"))
print(format(45,"<5d"))
print(format(0.457467657,"<9.3%"))
'''

##Question3 ##

name = input("Enter employee's name: ")
hour = eval(format(eval(input("Enter number of hours worked in a week: ")),".1f"))
pay_rate = eval(input("Enter hourly pay rate: "))

gross = hour * pay_rate

fed_rate = eval(input("Enter federal tax withholding rate: "))
fed_rate_1 = format(fed_rate,"4.1%")
fed_withhold = gross * fed_rate


sta_rate = eval(input("Enter state tax withholding rate: "))
sta_rate_1 = format(sta_rate,"3.1%")
sta_withhold = int(gross * sta_rate * 100) / 100
sta_withhold_1 = gross * sta_rate


Total_dedu = fed_withhold + sta_withhold
net_pay = gross - (fed_withhold + sta_withhold_1)

print("Employee name : " + name)
print("Hours Worked : ",hour)
print("Pay Rate : " + "$",pay_rate )
print("Gross Pay : " + "$",gross )



print("Deductions: ")
print("\t Federal Withholding("+fed_rate_1+ "): "+"$",fed_withhold)
print("\t State Withholding("+sta_rate_1+ "): " + "$",sta_withhold)
print("\t Total Deduction: " + "$",Total_dedu)
print("Net Pay : " + "$" + format(net_pay,".2f"))

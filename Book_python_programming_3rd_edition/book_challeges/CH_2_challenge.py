#! /usr/bin/env/python3

# 1. Create a list of illgegal variable

# Complete list of reserved words Can't use below variable.
"""
and
del
from
not
while
as
elif
global
or
with
assert
else
if
pass
yield
break
except
import
print
class
exec
in
raise
continue
finally
is
return
def
for
lambda
try
True # Python 3 onwards
False # Python 3 onwards
None  # Python 3 onwards
nonlocal # Python 3 onwards
async # in Python 3.7
await # in Python 3.7

So, you cannot use any of the """

# 2. Write program that allows a user to enter his 2 favorite foods. the program should then print out the name of a new food by joining the original food name together

# food1 = input("what is your 1st favorite food ?")
# food2 = input("what is your 2nd favorite food ?")
# print (food1,end=" ")
# print (food2)
# print ("\n this is new food name for you : ", food1,food2)  # Be careful of , between statement and variable
# print ("\n this is new food name for you : ", food1+food2)  # no space between food1 and food2



# 3. write a tipper program where the user enters a restaurant nill total. The program should then display two amount: a 15% tip and 20% tip.

# total = int(input("what is total bill ? :"))
# tip_15 = int(total * 0.15)
# tip_20 = int(total *0.20)
# print ("if you want to pay 15% tip, give this much: $",tip_15)
# print ("\nif you want to pay 20% tip, give this much: $",tip_20)

#4. write car salesman program where the user enters the base price of a car. The program should add on a bunch of extra fees such as tax
#   license,dealer prep, and destination charges. Make tax and license a percent of the base price. The other fees should be set value. Dispaly the actual price of the car once all the extras are applied.

base = int(input("what is base car price ?"))
tax = base * 0.1
license = int(300)
dealer_prep = int(100)
destination=int(50)

license_1 = license/tax

actual_price = base+tax+license+dealer_prep+destination
print ( "this is your actual car price..",actual_price)

print("this is license price percentage:",license_1,"%")
print("this is tax percentage 10%")



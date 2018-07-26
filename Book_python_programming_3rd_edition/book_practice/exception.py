'''
## waiting for number, any other alphabet also OK. it store to num variable
num = input("what is your fav number ? \n")
print(num)

## this one make whatever received number store as integer, if you type not number it will give you error
num_1 = int(input("what is your fav number ? \n"))
print(num_1)
'''
## This code give you even if you type alphabet indtead of number it will not give you error
while True:
    try:
        number = int(input("what is your fav number ? \n"))
        print (2/number)  # if this case if the input is "0" it also give you error
        break
    except ValueError:
        print ("Pls make sure enter number...")
    except ZeroDivisionError:
        print ("pls do not pick '0'")
    except:    #### General exception if you don't know what is error code
        break
    finally:
        print("loop complete")
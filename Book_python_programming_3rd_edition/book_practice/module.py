import mod  ### this is call the file name mod you don't need specify .py ####
import random  ## import random Liberary, this Lib create just random number. it is located c:/program files/python 3.5/Lib/
mod.fish()  ## if mod file has fish() in the last,which means it has print function there.so it just need call the file but if mod file doesn't have fish()
             ## this file need call the function. but it called fish() it doens't work, it has to specify file name as well, so it need define mod.fish()


x = random.randrange(1, 100)  # this one keep create random number even if same input. if you keep run this program. it keep create different number.
print(x)
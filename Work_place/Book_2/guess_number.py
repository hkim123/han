###### 개인적으로 짠 프로그램 ####
import random
'''
secretNumber = random.randint(1,20)
print (secretNumber)
print('I am taking of number between 1 and 20')

number = ''
while True:
    number = input("Please enter your number : ")
    if int(number) == secretNumber:
        print ('GOOD Guess!!!! you got it!!!')
        break
    elif int(number) < secretNumber:
        print ('Your guess is low, please make high')
    elif int(number) > secretNumber:
        print('Your guess is high, please make low')
    else:
        print('Keep trying')
'''

#### 책 해답 프로그램 , Book2 page 97 #####

secretNumber_1 = random.randint(1,20)  ### 위의 변수와 이름이 같아서 _1 으로 변경
#Ask the player to guess 6 times.
for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber_1:
        print('Your guess is too low')
    elif guess > secretNumber_1:
        print('Your guess is too high')
    else:
        break
if guess == secretNumber_1:
    print('Good job ! You guessed my number in ' + str(guessesTaken) + ' guesses !')
else:
    print('Nope. The number I was thinking of was' + str(secretNumber_1))
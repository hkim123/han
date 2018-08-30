name = ""
while not name:  ########## name이 empty 이면 계속 물어본다
    print('Enter your name: ')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough room fo all your guests')
print('done')

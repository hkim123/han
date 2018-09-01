import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook no so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)


#### 위의 3 줄은 아래의 한줄로 바꿀수 있다 ####
#print(getAnswer(random.randint(1,9)))

##### print 는 return value 를 제공할 필요가 없다, 그러나 모든 함수는 다 리턴값을 제공해야 하므로 print 는 리탄값으로 None 을 제공한다 ###

spam = print('Hello')
print(spam)  #### None return
#None == spam

print ('abc','def',sep =',')
print ('abc','def',end ='!\n')
print ('abd',end ='')
print ('def')
print('925','337','7018',sep='-',end='!!!')

##### 변수 #####

def spam_1():
    print(eggs)
eggs = 42
spam_1()
print(eggs)


### 같은 이름의 지역 & 전역 변수 Not recommaned #####
def spam_2():
    aa = 'spam_2 local'
    print(aa)  #prints spam local
def bacon_2():
    aa = 'bacon local'
    print(aa)    # print 'bacon local'
    spam_2()     # print 'spam local'
    print(aa)    # print 'bacon local'

aa = 'global'
bacon_2()
print(aa)

##### global variable and local variable #####
### change global variable from local variable

def spam_3():
    global bb
    bb = 'spam_3'  # this is global
def bacon_3():
    bb = 'bacon'   # this is local
def ham():
    print(bb)      # this is global

bb = 42  # this is global
spam_3()
print(bb)
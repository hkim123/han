#collections.namedtuple() : 튜플 객체에 이름을 설정하는 함수

from collections import namedtuple

Member = namedtuple('Member',['email','date'])
member1 = Member('asdf@naver.com','2014-10-04')
print(member1)
print(member1.email)
print(member1.date)

print(len(member1))

email, date = member1
print(email)
print(date)

stock_rec = [
    ("samsung", 10, 100),
    ("hyundai", 10, 90),
    ("kia", 10, 80)
]
def cal_stock(stock):
    tot = 0
    for n in stock:
        tot += n[1] * n[2]  #1과 2의 의미를 알수 없기 때문에 namedtuple 을 사용한다
    return tot

print(cal_stock(stock_rec))


Stock = namedtuple('Stock', ['name', 'amount','price'])

def cal_stock(stock):
    tot = 0
    for n in stock:
        s = Stock(*n)
        tot += s.amount* s.price
    return tot

print(cal_stock(stock_rec))

n1 = ("samsung", 10, 100)
print(*n1)  #각각의 n을 분리한다
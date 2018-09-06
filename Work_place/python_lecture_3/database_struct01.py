#database 자료를 list 에 옮겨와 저장후 정렬 시키는 방법

records = [
    {'id':'test','pw':'1234','name':'홍길동','hp':'010-1234-1234'},
    {'id':'test1','pw':'1234','name':'강호동','hp':'010-1225-1884'},
    {'id':'test2','pw':'1234','name':'이경규','hp':'010-1454-1984'},
    {'id':'test3','pw':'1234','name':'이문세','hp':'010-4334-1247'},
    {'id':'test4','pw':'1234','name':'이수근','hp':'010-1564-1234'},
    {'id':'test5','pw':'1234','name':'han','hp':'010-1247-4834'}
]

#모듈 operator.itemgetter

from operator import itemgetter
from pprint import pprint

rec_by_name = sorted(records, key=itemgetter('name'))
rec_by_id = sorted(records,key = itemgetter('id'))

pprint(rec_by_name)

rec_by_name_tel = sorted(records, key=itemgetter('name','hp'),reverse=True)
pprint(rec_by_name_tel)



#deque 자료구조를 응용, deque 는 양쪽에서 입력하고 빼낼수 있는 구조
#deque를 이용해서 고정크기의 큐를 생성하기 (maxlen = n)
from collections import deque
dQ = deque(maxlen = 4) #4개의 item 을 갖는 큐를 생성

dQ.append('aa')

dQ.append('bb')

dQ.append('cc')

dQ.append('dd')

print(dQ)

dQ.append('ee')  #deque 의 크기는 4 이므로 aa를 없애고, ee를 저장한다.

print(dQ)

def search_word(lines, find_word, history):
    previous_lines = deque(maxlen=history)
    for readline in lines:
        if find_word in readline:
            yield readline, previous_lines
        previous_lines.append(readline)
'''
with open('someText.txt') as f:
    fword = search_word(f, "좋은아침", 4)
    print(fword)
    print(next(fword))
'''

if __name__ == '__main__':
    with open('someText.txt') as f:
        for fline, preTexts in search_word(f, "좋은아침", 4):
            for preline in preTexts:
                print(preline)
            print(fline)
            print("="*20)



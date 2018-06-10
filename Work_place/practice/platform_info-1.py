# coding=utf-8
# 함수를 import 하지 않고 아래와 같이 from 을 쓰면 module.function() 형식으로 할 필요없이 그냥 function() 으로 사용 가능.
# 아래는 info.py 와 똑같은 기능을 함.
from platform import *
from multiprocessing import *

print system()
print platform()
print "version: ", version()
print "processor: ", processor()
print "number of cpu: ", cpu_count()
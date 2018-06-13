#!/usr/bin/python
# coding=utf-8
# 위의 coding=utf-8 은 한글 입력을 가능하게 해 줍니다. 아님 comment out 문장도 입력이 안됨.
# paltform 은 python 을 실행하는 운영체제를 보여줍니다.
# multiprocessing 은 CPU 개수를 보여줌.


import platform
import multiprocessing

print "운영체제: ", platform.system()
print "상세 정보: ", platform.platform()
print "version: ", platform.version()
print "프로세서: ", platform.processor()
print "CPU 수: ", multiprocessing.cpu_count()
print ("python 2.7 과 3.0 모두 됨")

print platform.machine()
print platform.node()
print platform.python_build()
print platform.python_compiler()
print platform.python_version()
print platform.uname()


print multiprocessing.current_process()

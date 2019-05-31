#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:00:33 2019

@author: hankim
"""

#### Create statuc route to border leaf ####

j= 5
for i in range(1,32):
    print('ip route vrf vrf_',i,' 0.0.0.0/0 10.',j,'.255.253',sep='')
    j = j + 4
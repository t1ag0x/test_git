#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from time import sleep

def christmas_time_already():
    print('nop, try again later')
    sleep(3600)

if __name__ == '__main__':
    c = 0
    while c <= 8000:
        christmas_time_already()
        c +=1

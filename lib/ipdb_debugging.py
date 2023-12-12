#!/usr/bin/env python3

import ipdb

def multiply(num):
    for index, value in enumerate(num):
        print(value,index)
        num[index]=value * 2
    return num


multiply([2,4,6])
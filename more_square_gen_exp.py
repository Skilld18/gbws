#!/usr/bin/python
from itertools import chain

def complete(state):
    return len(state) == 9

def valid(state):
    return len(state) == 0 or state[0] == 9

def get_valid(state):
    nums = set(range(1,10)) - set(state)
    nums = filter(lambda x: valid(state + [x]), nums)
    return sorted(list(nums))

def progress(state):
    global s1
    global s2
    global s3
    a = s1.index(state[0])
    b = len(s1)
    c = s2.index(state[1])
    d = len(s2)
    e = s3.index(state[2])
    f = len(s3)
    
    denom = b * d * f
    num = (a*d*f) + (c*f) + e
    return num/denom
    

def recurse(stack):
    v = get_valid(stack)
    if len(stack) == 0:
        global s1
        s1 = v
    if len(stack) == 1:
        global s2
        s2 = v
    if len(stack) == 2:
        global s3
        s3 = v
    for i in v:
        yield from recurse(stack + [i])
    if complete(stack):
        yield stack


s1 = 0
s2 = 0
s3 = 0
stack = []
for i in recurse(stack):
    print(i)
    print(progress(i))



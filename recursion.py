#!user/bin/env python
# -*- coding: utf-8 -*-


def fibonacci(n):
    if n < 2:
        return n
    elif n < 0:
        print ('Number must be greater than Zero.')
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
    try:
        if b > a:
            return gcd(b, a)
        if a % b == 0:
            return b
        return gcd(b, a % b)
    except Exception as e:
        return e

def compareTo(s1, s2):
    negative = -1
    even = 0
    positive = 1

    for i1 in s1:
        s1sum = len(s1 + i1)

    for i2 in s2:
        s2sum = len(s2 + i2)

    if s1sum == s2sum:
        print even
    elif s1sum < s2sum:
        print negative
    elif s1sum > s2sum:
        print positive

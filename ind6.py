#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def foo(t):
    def inner(s):
        if t == list:
            return list(map(int, s.split()))
        return tuple(map(int, s.split()))

    return inner

if __name__ == '__main__':
    print(foo(list)('1 2 3 4'))
    print(foo(tuple)('1 2 3 4 5'))

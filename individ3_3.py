#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    while True:
        n = int(input('Введите сумму: = '))
        res = 0
        for k in reversed([1, 2, 5, 10, 100, 500]):
            m, n = divmod(n, k)
            print(f'Купюра {k} * {m}')
            res += m
        print(res)
        print()

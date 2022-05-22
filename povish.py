#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

if __name__ == '__main__':
    def shi(series=0, elem=1, n=0):
        if elem < eps:
            return series, n
        if not n:
            elem = x
        else:
            elem *= x*x*(2*n-1)/(2*n*(2*n+1)*(2*n+1))
        return shi(series + elem, elem, n+1)
    
    x = 717
    eps = 1e-10
    print(shi())

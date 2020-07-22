# -*- coding: utf-8 -*-
L = [x * x for x in range(10)]

g = (x * x for x in range(10))
print(next(g))

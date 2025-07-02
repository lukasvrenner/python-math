#!/usr/bin/python3

import math

def integrand(x, y):
    return 2 * math.exp(x ** 3 - y ** 3)

def double_riemann(func, start_x, stop_x, shift_x, n: int, start_y, stop_y, shift_y, m: int):
    delta_x = (stop_x - start_x) / n
    delta_y = (stop_y - start_y) / m
    sum = 0
    for i in range(n):
        for j in range(m):
            sum += func(start_x + (i + shift_x) * delta_x, start_y + (j + shift_y) * delta_y)
    sum *= delta_x * delta_y
    return sum

print("volume:", double_riemann(integrand, start_x=0, stop_x=1, shift_x=0, n=116, start_y=0, stop_y=1, shift_y=0, m=116))



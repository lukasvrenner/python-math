#!/usr/bin/python3

import math

def integrand(x):
    return math.sqrt((-math.sin(x)) ** 2 + (math.cos(x)*math.exp(math.sin(x))) ** 2)


def riemann_sum(func, lower, upper, n: int, shift):
    delta_x = (upper - lower) / n
    sum = 0
    for i in range(n):
        sum += func(lower + (i + shift) * delta_x)
    sum *= delta_x
    return sum

def trapezoid(func, lower, upper, n: int):
    delta_x = (upper - lower) / n

    sum = 0
    for i in range(1, n):
        sum += func(lower + i * delta_x)
    sum *= 2

    sum = func(lower) + sum + func(upper)
    return sum * delta_x / 2

def simpsons(func, lower, upper, n: int) -> float:
    assert n & 1 == 0, "n must be even"
    delta_x = (upper - lower) / n

    mul_four_sum = 0
    for i in range(1, n, 2):
        mul_four_sum += func(lower + i * delta_x)
    mul_four_sum *= 4

    mul_two_sum = 0
    for i in range(2, n, 2):
        mul_two_sum += func(lower + i * delta_x)
    mul_two_sum *= 2

    sum = func(lower) + mul_four_sum + mul_two_sum + func(upper)
    return sum * delta_x / 3

print("left:", riemann_sum(integrand, lower=1, upper=4, n=5, shift=0))
print("middle:", riemann_sum(integrand, lower=0, upper=4 * math.pi, n=10, shift=0.5))
print("right:", riemann_sum(integrand, lower=1, upper=4, n=5, shift=1))
print("trapezoid:", trapezoid(integrand, lower=0, upper=math.pi, n=6))
print("simpsons:", math.pi * 2 * simpsons(integrand, lower=0, upper=math.pi, n=6))

#!/usr/bin/python3

def summand(x):
    return x ** (1/2)

def riemann_sum(func, lower, upper, n: int, shift):
    delta_x = (upper - lower) / n
    sum = 0
    for i in range(n):
        sum += func(lower + (i + shift) * delta_x)
    sum *= delta_x
    return sum

print("left:",riemann_sum(summand, lower=0, upper=10000, n=10000, shift=0))
print("middle:", riemann_sum(summand, lower=0, upper=10000, n=10000, shift=0.5))
print("right:", riemann_sum(summand, lower=0, upper=10000, n=10000, shift=1))

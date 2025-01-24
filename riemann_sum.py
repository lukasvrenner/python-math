#!/usr/bin/python3

def summand(x):
    return 5 * x ** 2

def riemann_sum(func, lower, upper, n: int, shift):
    delta_x = (upper - lower) / n
    sum = 0
    for i in range(n):
        sum += func(lower + (i + shift) * delta_x)
    sum *= delta_x
    return sum

def simpsons(func, lower, upper, n: int):
    assert(n & 1 == 0)
    delta_x = (upper - lower) / n

    mul_four_sum = 0
    for i in range(1, n, 2):
        sub = 2 * i + 1
        print(sub)
        mul_four_sum += func(lower + i * delta_x)
    mul_four_sum *= 4

    mul_two_sum = 0
    for i in range(2, n, 2):
        mul_two_sum += func(lower + i * delta_x)
    mul_two_sum *= 2

    sum = func(lower) + mul_four_sum + mul_two_sum + func(upper)
    return sum * delta_x / 3

print("left:", riemann_sum(summand, lower=8, upper=10, n=4, shift=0))
print("middle:", riemann_sum(summand, lower=8, upper=10, n=4, shift=0.5))
print("right:", riemann_sum(summand, lower=8, upper=10, n=4, shift=1))
print("simpsons:", simpsons(summand, lower=8, upper=10, n=4))

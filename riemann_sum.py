def func_1(x):
    return -(x**2)/4 + 2*x

def riemen_sum(func, lower, upper, n: int, shift):
    delta_x = (upper - lower) / n
    sum = 0
    for i in range(n):
        sum += func(lower + (i + shift) * delta_x)
    sum *= delta_x
    return sum

print("left:",riemen_sum(func_1, lower=3, upper=7, n=8, shift=0))
print("middle:", riemen_sum(func_1, lower=3, upper=7, n=8, shift=0.5))
print("right:", riemen_sum(func_1, lower=3, upper=7, n=8, shift=1))

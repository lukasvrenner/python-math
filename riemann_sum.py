def func_1(x):
    return -(x**2)/4 + 2*x

def riemann_sum(func, lower, upper, n: int, shift):
    delta_x = (upper - lower) / n
    sum = 0
    for i in range(shift, n + shift):
        sum += func(lower + i * delta_x)
    sum *= delta_x
    return sum

print(riemann_sum(func_1, lower=3, upper=7, n=8, shift=0))
print(riemann_sum(func_1, lower=3, upper=7, n=8, shift=1))

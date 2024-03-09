def f(n, ban):
    if n > 1000:
        return 0
    if n == 1000:
        return 1
    s = 0
    s += f(n + 3, 1)
    if ban == 0:
        s += f(n * 5, 0)
    s += f(n * 7, 0)
    return s


print(f(1, 0))
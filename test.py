from functools import lru_cache


@lru_cache(None)
def f(n, ban):
    if n > 50:
        return 0
    if n == 50:
        return 1
    s = 0
    s += f(n + 1, 1)
    if ban == 0:
        s += f(n * 2, 0)
    s += f(n + 2, 0)
    return s


print(f(1, 0))
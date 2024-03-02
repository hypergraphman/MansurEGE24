def f(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return 3 + f(n // 2 - 1)
    if n > 1 and n % 2 != 0:
        return n + f(n + 2)


k = 0
for n in range(1, 1000):
    try:
        if f(n) == 19:
            print(n)
    except :
        pass
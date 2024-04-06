def n_to_3(n):
    r = ''
    while n > 0:
        r = str(n % 3) + r
        n //= 3
    return r if r else '0'


def f(n):
    s1 = n_to_3(n)
    s2 = s1 + n_to_3(s1.count('2'))
    s3 = s2 + n_to_3(s2.count('1'))
    s4 = s3 + n_to_3(s3.count('0'))
    return int(s4, 3)


print(f(5))  # проверка условия

for i in range(5, 1000):
    if f(i) < 1000:
        print(i)

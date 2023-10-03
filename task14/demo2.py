from string import ascii_uppercase, digits


def n_to_p(n, p):
    r = ''
    a = digits + ascii_uppercase
    while n > 0:
        r = a[n % p] + r
        n //= p
    return r


num = n_to_p(3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2 * 25**4 - 1999, 25)
print(num)
print(num.count('0'))
def divs(n):
    r = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            r.add(d)
            r.add(n // d)
    return sorted(r)


from fnmatch import fnmatch

for i in range(1, 10**7):
    if fnmatch(str(i), '3*52?') and len(divs(i)) % 2 != 0:
        print(i, divs(i)[-2])

# 18944
from itertools import product

count = 0
for d1 in '2468':
    for d2 in '012345678':
        for d3 in '012345678':
            for d4 in '012345678':
                for d5 in '0234567':
                    num = d1 + d2 + d3 + d4 + d5
                    if num.count('3') <= 1:
                        count += 1
print(count)

a = [''.join(x) for x in product('012345678', repeat=5)]
count = 0
for num in a:
    if num[0] in '2468' and num.count('3') <= 1 and num[-1] not in '18':
        count += 1
print(count)
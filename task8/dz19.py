from itertools import permutations

a = set([''.join(x) for x in permutations('kompilytr', r=6)])
k = 0
for word in a:
    if word[-1] == 'r':
        k += 1
print(k)
from itertools import product, permutations


for word in product('ab', repeat=2):
    print(''.join(word))
print('-----')
for word in permutations('aA', r=3):
    print(''.join(word))
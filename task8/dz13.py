from itertools import permutations

k = 0
for word in permutations('PRIKAZ', r=4):
    word = ''.join(word)
    if word.count('A') + word.count('I') <= 1:
        k += 1
print(k)
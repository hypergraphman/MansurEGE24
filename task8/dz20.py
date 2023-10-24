from itertools import product

k = 0
words = product('ONIKS', repeat=4)
for word in words:
    word = ''.join(word)
    if word.count('S') == 3 and word.count('O') == 1:
        k += 1
words = product('ONIKS', repeat=5)
for word in words:
    word = ''.join(word)
    if word.count('S') == 3 and word.count('O') == 1:
        k += 1
words = product('ONIKS', repeat=6)
for word in words:
    word = ''.join(word)
    if word.count('S') == 3 and word.count('O') == 1:
        k += 1
print(k)
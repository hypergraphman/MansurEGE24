k = 0
for i in range(1, 10**9):
    if i % 10 ** 6 == 0:
        print(i // 10 ** 6)
    if bin(i).count('0') == 5:
        k += 1
print(k)
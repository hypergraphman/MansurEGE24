s = open('24-4.txt').read().strip()
c = [0] * 26
for i in range(3, len(s)):
    abc = s[i - 3] + s[i - 2] + s[i - 1]
    if abc == 'ABC':
        c[ord(s[i]) - ord('A')] += 1
mn = float('inf')
mn_let = None
for i in range(len(c)):
    if c[i] != 0 and c[i] < mn:
        mn = c[i]
        mn_let = chr(ord('A') + i)
print(mn, mn_let)
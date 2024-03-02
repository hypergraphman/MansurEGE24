s = open('24-3.txt').read()
k = 0
for i in range(len(s) - 2):
   if s[i] + s[i + 1] + s[i + 2] == 'KTO':
       k += 1
print(k)
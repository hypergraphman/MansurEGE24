from collections import Counter

s = open('24-8.txt').read()
mx_line = ''
mx = 0
for line in s.split('\n'):
    m = 0
    c = 1
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            c += 1
        else:
            c = 1
        m = max(m, c)
    if m > mx:
        mx = m
        mx_line = line

counter = Counter(mx_line)
print(counter)
print(list(counter.most_common()))
print('K', s.count('K'))
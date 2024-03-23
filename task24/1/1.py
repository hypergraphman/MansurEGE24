from string import ascii_uppercase

f = open('24-3.txt')
mx = 0
for line in f:
    if line.count('E') < 20:
        for let in ascii_uppercase:
            mx = max(line.rfind(let) - line.find(let), mx)
print(mx)

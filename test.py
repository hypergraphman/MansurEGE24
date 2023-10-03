num = '987654'
s = num[:-6:-1]
if len(num) == 6:
    s = num[-6] + s
print(int(s))
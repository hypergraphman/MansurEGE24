s = open('24.txt').readline()

alp = '0123456789ABCDEF'

cur_len = 0
max_len = 0
num = ''
max_num = None
for el in s:
    if el in alp:
        cur_len += 1
        num += el
    else:
        cur_len = 0
        num = ''
    if cur_len > max_len:
        max_len = cur_len
        max_num = num
print(max_len, max_num, int(max_num, 16))
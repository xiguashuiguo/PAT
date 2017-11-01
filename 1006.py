# ！usr/bin/env python3

num = input()
n=int(num)
if n < 99:
    num = '0' + str(num)
if n < 9:
    num = '0' + num
bai = int(num[0])
shi = int(num[1])
ge = int(num[2])
tmp = bai * 'B' + shi * "S"
for i in range(ge):
    tmp = tmp + str(i + 1)
print(tmp)

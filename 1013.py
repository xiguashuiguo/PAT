import math

raw = input()
rawf = raw.split()
n, m = int(rawf[0]), int(rawf[1])
# m=int(rawf[0])
# n=int(rawf[1])
out = ""


# 判断是否是素数；同时及一个数被所有小于他的数去整除，这里没有优化
def su(n):
    # if prime number
    if n <= 1:
        return False
    for x in range(2, int(math.sqrt(n)) + 1):  # 迭代器range()替换为素数列表，减少运算
        if n % x == 0:
            return False
    return True


def su_creat():
    adder = 1
    while True:
        adder += 2
        if su(adder):
            yield adder


# 素数循环生成器-未来考虑做一个可迭代对象、类
f = su_creat()
content = [2]
while len(content) < max(m, n):
    content.append(next(f))

# 得到前max(m,n)个素数
content = content[min(m, n) - 1:max(m, n)]

# print(content)输出对应的格式
for each in content:
    out += ' ' + str(each)
    if (content.index(each) + 1) % 10 == 0:
        print(out.strip())
        out = ''
if len(out) > 0:
    print(out.strip())

def form(s):
    tmp = ''
    if s < 0:
        tmp += '-'
        s = -s
    s1 = str(s)
    st = ''
    i = 1
    while i <= len(s1):
        if (i - 1) % 3 == 0 and i > 1 :
            st = s1[-i] + ',' + st
            i += 1
        else:
            st = s1[-i] + st
            i += 1
    return tmp + st


s = input()
s = s.split()
a, b = int(s[0]), int(s[1])
s = a + b
print(form(s))

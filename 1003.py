# -*- coding: utf-8 -*-
def Match(s):
    s=str(s)
    if s.find('P')==-1 or s.find('T')==-1:
        return False
    a=s.split('P',1)[0]
    if a.count('A')!=len(a):
        return False
    c=s.split('T',1)[1]
    if c.count('A')!=len(c):
        return False
    b=s[len(a)+1:len(s.split('T',1)[0])]
    if b=='':
        return False
    if a==c and b=='A':
        return True
    else:
        b=b[0:len(b)-1]
        c=c[0:len(c)-len(a)]
        s=a+'P'+b+'T'+c
        return Match(s)


n=input()
for i in list(range(0,int(n))):
    s=input()
    if Match(s):
        print("YES")
    else:
        print("NO")
#s='A'
#if Match(s):
#    print("YES")
#else:
#    print("NO")

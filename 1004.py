# encoding=utf-8

n=input()
n=int(n)
info={}
grade=[]
for i in range(n):
    tmp=input()
    name=str(tmp).split(' ',3)[0]
    xuehao=str(tmp).split(' ',3)[1]
    chengji=int(str(tmp).split(' ',3)[2])
    grade.append(chengji)
    info[chengji]=[name,xuehao]
grade.sort()
print(info[grade[-1]][0]+' '+info[grade[-1]][1])
print(info[grade[0]][0]+' '+info[grade[0]][1])

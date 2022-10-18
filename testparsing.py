import re
#Тест регекса возвращаем массив
f=open('brief.txt','r')
f.readline()
regex=r'(\S+) +(\S+) +\w+ \w+ +(up|down|administratively down) +(up|down)'
int_list=[]
for line in f:
    mas=[m.groups() for m in re.finditer(regex,f.read())]
f.close()

#Пишим интерфейсы в файл
e=open('int.txt','w')
for i in range(len(mas)-1):
    e.write(mas[i][0]+'\n')
e.close()


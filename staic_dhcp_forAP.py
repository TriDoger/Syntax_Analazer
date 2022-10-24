# Использует вывод команды с контролера
# sh ap config general | i AP Name | AP Identifier | Netmask  | IP | Gateway IP Address
# Который парсит в готовый конфиг dhcp резервации
#Код дико кривой и не уверсальный Ж)

template='''
ip dhcp pool {name}
   host {ip} {mask}
   client-identifier 01{mac}
   default-router {router}
   dns-server 172.16.60.18 172.16.60.34
 option 43 hex f104.c0a8.e859
 lease infinite
'''
keys=['Cisco AP Name','Cisco AP Identifier','IP Address','IP Netmask','Gateway IP Address']
e=open('test.txt','r')
tmp=[]
ext=[]
tmp2 = dict.fromkeys(keys,0)
j=0
i=0
for strs in e:
    tmp = list(map(lambda str: str.strip(), strs.split(":")))
    if tmp[0]=='Cisco AP Name' or tmp[0]=='Cisco AP Identifier' \
            or tmp[0]=='IP Address' or tmp[0]=='IP Netmask'\
            or tmp[0]=='Gateway IP Address':
        i+=1
        tmp2[tmp[0]]=tmp[1]
        if i==5:
            i=0
            print('clear ip dhcp binding {ip}'.format(ip=tmp2['IP Address']))
            print('conf t')
            print(template.format(name=tmp2['Cisco AP Name'],ip=tmp2['IP Address'],
                                 mac=tmp2['Cisco AP Identifier'],mask=tmp2['IP Netmask'],router=tmp2['Gateway IP Address']))
e.close()
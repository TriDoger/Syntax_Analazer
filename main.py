import getpass
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
# username=input('Username: ')
# password=getpass.getpass()
# cisco_router = {
#     'device_type': 'cisco_ios',
#     'host': '',
#     'username': username,
#     'password': password,
#     'port': 22,
# }
# ssh = ConnectHandler(**cisco_router)
# ssh.enable()

#Тестовая запись таблицы
# res=ssh.send_command('show ip int br')
# f=open('brief.txt','w')
# for str in res:
#     f.write(str)
# f.close()
# print(res)


res=''
e=open('int.txt','r')
for int in e:
    print(('sh ipv6 traffic int '+int))
e.close()
print(res)

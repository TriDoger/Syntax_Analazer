import getpass
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
username=input('Username: ')
password=getpass.getpass()
cisco_router = {
    'device_type': 'cisco_ios',
    'host': '10.185.2.3',
    'username': username,
    'password': password,
    'port': 22,
}
print(*cisco_router)
ssh = ConnectHandler(**cisco_router)
# ssh.enable()

#Тестовая запись таблицы
print(ssh.send_command('show ip int br'))
print()
ssh.disconnect()
# f=open('brief.txt','w')
# for str in res:
#     f.write(str)
# f.close()
# print(res)

# Тестовая создание команд
# res=''
# e=open('int.txt','r')
# for int in e:
#     print(('sh ipv6 traffic int '+int))
# e.close()
# print(res)

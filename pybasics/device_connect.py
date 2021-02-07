from netmiko import ConnectHandler
from getpass import getpass
device1 = {
     "host": "l3swa",
     "username": "cisco",
     "password": "123!Cisco",
     "device_type": "cisco_ios",
          }

device2 = {
     "host": "rtra",
     "username": "cisco",
     "password": "123!Cisco",
     "device_type": "cisco_ios",
          }

for device in (device1,device2):
    connect_device = ConnectHandler(**device)
    print(connect_device.find_prompt())

connect_device.disconnect()

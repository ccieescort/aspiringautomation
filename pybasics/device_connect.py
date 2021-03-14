from netmiko import ConnectHandler

device1 = {
     "host": "rtra",
     "username": "cisco",
     "password": "123!Cisco",
     "device_type": "cisco_ios",
          }

device2 = {
     "host": "rtrb",
     "username": "cisco",
     "password": "123!Cisco",
     "device_type": "cisco_ios",
          }

for device in (device1,device2):
    connect_device = ConnectHandler(**device)
    print(connect_device.find_prompt())

connect_device.disconnect()

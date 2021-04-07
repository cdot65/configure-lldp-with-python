from jnpr.junos import Device
from jnpr.junos.utils.config import Config


device_connection = Device(host='dallas-fw0', user='automation', password='juniper123').open()

with Config(device_connection, mode='exclusive') as device_config:
    device_config.load('set protocols lldp interface all', format='set')
    device_config.pdiff()
    device_config.commit()

device_connection.close()

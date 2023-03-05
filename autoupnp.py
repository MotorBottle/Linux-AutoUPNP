# -*- coding = utf-8 -*-
# @Time : 2023/2/21 14:24
# @Author : MotorBottle
# @File : autoupnp.py
# @Software : PyCharm

import miniupnpc
import time

# 创建MiniUPnP客户端对象
upnp = miniupnpc.UPnP()

# 发现IGD设备并获取其控制URL
upnp.discoverdelay = 200
upnp.discover()
upnp.selectigd()

# 初始化上一次的外部IP地址
ip_file_path = "~/upnp/ip.txt"

try:
   with open(ip_file_path, "r") as f:
       last_external_ip_address = f.read().strip()
except FileNotFoundError:
   last_external_ip_address = ""


port_mappings = [
    # 外部端口号，内部端口号，协议，备注----如有多条自己往下添加即可
    {"external_port": 10900, "internal_port": 9000, "protocol": "TCP", "description": "Portainer"},
    {"external_port": 18876, "internal_port": 9876, "protocol": "TCP", "description": "DDNS"},
]


# 获取当前的外部IP地址
external_ip_address = upnp.externalipaddress()

# 如果外部IP地址发生更改，执行端口映射
if external_ip_address != last_external_ip_address:
    # 执行端口映射
    for mapping in port_mappings:
        external_port = mapping["external_port"]
        internal_port = mapping["internal_port"]
        protocol = mapping["protocol"]
        description = mapping["description"]
        duration = 0
        upnp.addportmapping(external_port, protocol, upnp.lanaddr, internal_port, description, None)

        # 输出结果
        print(f"Port {external_port} ({protocol}) mapped to {upnp.lanaddr}:{internal_port}")

    # 更新上一次的外部IP地址
    last_external_ip_address = external_ip_address

    with open(ip_file_path, "w") as f:
       f.write(external_ip_address)
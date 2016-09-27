#根据输入的IP或网络地址段返回网络、掩码、广播、反向解析等
#!/usr/bin/env python

from IPy import IP

ip_s = raw_input('Please input an IP or net-range: ') #接受用户输入，参数为IP地址或网段地址
ips = IP(ip_s)


if len(ips) > 1: #如果是一个网络地址段
    print('net: %s' % ips.net())  #输出网络地址
    print('netmask: %s' % ips.netmask())  #输出子网掩码地址
    print('broadcast: %s' % ips.broadcast())  #输出广播地址
    print('reverse address: %s' % ips.reverseNames()[0])  #输出地址的反向解析
    print('subnet: %s' % len(ips))  #输出子网数目
else:  #如果是单个IP地址
    print('reverse address: %s' % ips.reverseNames()[0]) #输出IP反向解析

print('hexadecimal: %s' % ips.strHex())  #输出十六进制地址
print('binary ip: %s' % ips.strBin())    #输出二进制地址
print('iptype: %s' % ips.iptype())       #输出地址类型，PRIVATE、PUBLIC、LOOPBACK

>>> from socket import *
>>> fd = socket(AF_INET, SOCK_DGRAM)
>>> fd.sendto('hello dear', ('127.0.0.1',3000))
10
>>> 





>>> from socket import *
>>> fd = socket(AF_INET, SOCK_DGRAM)
>>> fd.bind(('127.0.0.1',3000))
>>> fd.recvfrom(1000)
('hello dear', ('127.0.0.1', 45841))
>>> 


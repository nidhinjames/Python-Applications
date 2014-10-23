#client-program 
from socket import *
def send():
	message = raw_input("Enter the message:::>>>>")
	fd = socket(AF_INET, SOCK_DGRAM)
	fd.sendto(message , ('127.0.0.1',3000))

def receive():

	fd = socket(AF_INET, SOCK_DGRAM)
        fd.bind(('127.0.0.2',3002))
	a = fd.recvfrom(1000)
	print "Message from B::"
	print a



send()
receive()

import socket
from datetime import datetime


net=raw_input("Enter IP: ")
net1=net.split('.')
a='.'
net2=net1[0]+a+net1[1]+a+net1[2]+a
st=int(raw_input("Starting Number: "))
en=int(raw_input("Ending Number: "))
en+=1
t1=datetime.now()

def scan(addr):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=sock.connect_ex((addr,135))
        if result==0:
            return 1
        else:
            return 0

def run():
    for ip in xrange(st,en):
        addr=net2+str(ip)
        if(scan(addr)):
            print addr, " is live "

run()
t2=datetime.now()
print "Scanning completed in : ", (t2-t1)

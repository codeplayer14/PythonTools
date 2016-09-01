import os
import platform
from datetime import datetime
net=raw_input("Enter Network Address : ")
net1=net.split('.')
a='.'
net2=net1[0]+a+net1[1]+a+net1[2]+a

st1= int(raw_input("Enter starting number : "))
en1= int(raw_input("Enter ending number: "))
en1+=1

oper=platform.system()

if(oper=="Windows"):
    ping1="ping -n 1 "
elif(oper=="Linux"):
    ping1="ping -c 1 "
t1=datetime.now()
print "Scanning in Progress"


for ip in xrange(st1,en1):
    addr=net2+str(ip)
    comm=ping1+addr
    response = os.popen(comm)
    for line in response.readlines():
        if(line.count("ttl")):
            break;
    if(line.count("ttl")):
        print addr, "--> LIVE"

t2=datetime.now()

print "Scan Completed in : " , (t2-t1)
import os
import platform
import socket
import subprocess
import sys
import threading
import collections
from datetime import datetime

'''Section 1'''

net=raw_input("Enter network Address : ")
net1=net.split('.')
a= '.'
net2=net1[0]+a+net1[1]+a+net1[2]+a

st1=int(raw_input("Enter starting Address: "))
en1=int(raw_input("Enter ending Address: "))
en1+=1
dic=collections.OrderedDict()
oper=platform.system()

if(oper=="Windows"):
    ping1= "ping -n 1"
elif (oper=="Linux"):
    ping1=" ping -c 1"
else:
    ping1=" ping -c 1"
t1=datetime.now()
'''Section 2 - Coding the Thread'''

class myThread(threading.Thread):
    def __init__(self,st,en):
        threading.Thread.__init__(self)
        self.st=st
        self.en=en
    def run(self):
        run1(self.st,self.en)


def run1(st,en):
    #print "Scanning in Progress"
    for ip in xrange(st,en):
        addr=net2+str(ip)
        comm=ping1+addr
        response=os.popen(comm)
        for line in response.readlines():
            if line.count("TTL"):
                break
        if(line.count("TTL")):
            print addr , " -> LIVE"
            dic[ip]=addr

'''Section 4- Thread handling'''

total_ip= st1-en1
tn=20
total_thread=total_ip/tn

threads=[]
try:
    for i in xrange(total_thread):
        en=st1+tn
        if(en>en1):
            en=en1
        thread=myThread(st1,en)
        thread.start()
        threads.append(thread)
        st1=en
except:
    print "Error. Unable to Start thread"

print "\t","Number of threads active:  ", threading.activeCount()

for t in threads:
    t.join()

print "Exiting Main Thread"
dict= collections.OrderedDict(sorted(dic.items()))
for key in dict:
    print dict[key] , " --> " " Live"
t2=datetime.now()

print "Scanning completed in : ", (t2-t1)
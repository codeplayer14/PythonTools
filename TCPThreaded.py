from datetime import datetime
import socket,sys,subprocess
import collections
import threading
import thread
import time

net=raw_input("Enter the Network Address : ")
st=int(raw_input("Starting Address: "))
en=int(raw_input("Last Address : "))
en=en+1

dict = collections.OrderedDict()
net1=net.split('.')
a='.'
net2=net1[0]+a+net1[1]+a+net1[2]+a
t1=datetime.now()

'''Section 2'''


class myThread(threading.Thread):
    def __init__(self,st,en):
        threading.Thread.__init__(self)
        self.st=st
        self.en=en
    def run(self):
        run1(self.st,self.en)


'''Section 3'''
def scan(addr):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result=sock.connect_ex((addr,23249))
    if result==0:
        sock.close()
        return 1
    else:
        sock.close()


def run1(st1,en1):
    for ip in xrange(st1,en1):
        addr=net2+str(ip)
        if(scan(addr)):
            dict[ip]=addr


'''Section 4'''

total_ip=en-st
tn=20
total_thread=total_ip/tn
total_thread+=1
threads=[]

try:
    for i in xrange(total_thread):
        en1=st+tn
        if(en<en1):
            en1=en
        thread=myThread(st,en)
        thread.start()
        threads.append(thread)
        st=en
except:
    print "Error unable to start Thread"
print "\t Number of active threads: ", threading.activeCount()
for t in threads:
    t.join()
print "Exiting Main Thread"

dic= collections.OrderedDict(sorted(dict.items()))

for key in dic:
    print dic[key], "--> ", "Live"

t2=datetime.now()

print "Scanning Completed in : ", (t2-t1)


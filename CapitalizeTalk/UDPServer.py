import socket

def Main():
    ip="127.0.0.1"
    port=6333

    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((ip,port))

    print ("Server Started")
    while True:
        data,addr= sock.recvfrom(1024)
        data=data.decode("utf-8")
        print "Message from : " + str(addr)
        print "From connected user: " + data

        data=data.upper()
        print ("Sending : "+data)

        sock.sendto(data.encode("utf-8"),addr)

    sock.close()

if __name__ == '__main__':
    Main()
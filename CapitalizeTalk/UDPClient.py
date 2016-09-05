import socket

host="127.0.0.1"
port=5001
server=(host,6333)
def Main():
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock.bind((host,port))

    message=raw_input("->")
    while message!= 'q':
        sock.sendto(message.encode("utf-8"),server)

        data,addr =  sock.recvfrom(1024)

        print ("Received from server : "+ data)
        message= raw_input('->')

    sock.close()

if __name__ == '__main__':
    Main()
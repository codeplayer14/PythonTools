import socket


def Main():
    host='127.0.0.1'
    port= 6333

    sock=socket.socket()
    sock.bind((host,port))
    sock.listen(1)

    client,addr=sock.accept() #returns a tuple

    print "Connection from : " + str(addr)

    while(True):
        data=client.recv(1024).decode("utf-8") #decode data received as bytes
        if not data:
            break

        print "From connected user: " + data

        data=data.upper()

        print "Sending data : " + data

        client.send(data.encode("utf-8"))



    client.close()

if __name__== "__main__":
    Main()


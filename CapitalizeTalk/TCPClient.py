import socket

def Main():

    host='127.0.0.1'
    port= 6333

    sock=socket.socket()

    data=sock.connect((host,port))

    message=raw_input("->")

    while message != 'quit':
        sock.send(message.encode("utf-8"))
        data=sock.recv(1024).decode("utf-8")
        print  ("Received from server " + data)
        message=raw_input("->")
    sock.close()


if __name__ == '__main__':
    Main()


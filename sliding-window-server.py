import socket 
import time
import random

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.bind(('',8080))
s.listen(5)

print 'server is waiting for connections..'
while True :
    conn, addr = s.accept()

    print 'connection is estb. addr :(%s , %s) '%addr

    data = conn.recv(4096)
    totalframe = int(data)

    time.sleep(1)
    ackframe = 0
    while ackframe<totalframe:
        data = conn.recv(4096)
        framerecv = int(data)
        
        if random.randint(0,10000)%2:
            print 'data frame is recv. with frame no. as %s'%framerecv
            ackframe = ackframe + 1
            conn.sendall('True')
        else:
            conn.sendall('False')
        time.sleep(1)
    print 'closing the server..'
    break
s.close()

    



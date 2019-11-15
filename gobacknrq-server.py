import socket 
import random
import time
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind(('',8080))
s.listen(10)
print 'waiting for new connection ..'
while True:
    conn , addr = s.accept()
    print 'Connection is estb. with addr :(%s , %s)'%addr
    while True :
        try :
            data = conn.recv(4096)
        except :
            print 'connection is close by the clinet'
            conn.close()
            break
        frame_recv = int(data)
        if random.randint(0 , 100000)%10:
            print '%s is recv.'%frame_recv
            conn.send('True')
        else :
            conn.send('False')
        time.sleep(1)
s.close()
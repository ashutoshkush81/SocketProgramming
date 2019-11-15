import socket
import time
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.bind(('',12312))

s.listen(10)

while True :
    conn ,addr = s.accept()

    print 'connection with the new client addr : (%s , %s)'%addr

    data = conn.recv(4086)
    conn.send("mil gaya")

    # print data

    newdata = int(data)

    print newdata 
    num = 0 
    while num < newdata:
        newdata1 = conn.recv(4096)
        
        print 'data is recv. ',newdata1
        time.sleep(1)

        num = num + 1
    s.close()
    break







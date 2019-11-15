import socket 
import time
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.connect(('',12312))

totalframe = 10

s.send(str(totalframe))
lauda =s.recv(382)
print lauda

totalack = 0

while totalack < totalframe :
    another = totalack + 1
    s.send(str(another))
    print '%s is ack.'%(totalack+1)
    time.sleep(1)
    totalack = totalack + 1



    # data = s.recv(4096)

    # newdata = int(data, 10)

    # if newdata == 1:
    #     print '%s is ack.'%totalack
    #     totalack = totalack + 1
    # else :
    #     print '%s is not ack'%totalack
s.close()

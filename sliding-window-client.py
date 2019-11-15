import socket
import time

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.connect(('',8080))

while True :
    try :
        data = raw_input("Enter the frame size : ")
        totalframe = int(data)
        break
    except :
        print 'error !! , please try again!'

print data
s.sendall(data)

time.sleep(1)

ackframe = 0

while ackframe < totalframe :
    send_data = str(ackframe + 1)
    print('%s frame is send '%send_data)
    s.sendall(send_data)
    recv_data = s.recv(4096)
    if recv_data =='True':
        ackframe = ackframe + 1
        print '%s frame is ack. '%ackframe

    else :
        print 'time out , resend frame again ..'
    time.sleep(1)
s.close()


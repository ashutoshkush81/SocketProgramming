import socket
import math
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('', 8080))
print 'waiting for new connection ..'
while True:
    try:
        data1 = str(raw_input("Enter the totalframe : "))
        data2 = str(raw_input("Enter the window size : "))
        totalframe1 = float(data1)
        windowsize = int(data2)
        break
    except:
        print 'try again..'
totalack = 0
totalwindow = math.ceil(totalframe1/windowsize)
totalframe = int(totalframe1)
while totalack < totalwindow :
    for i in range (1 , min(windowsize + 1 , totalframe - totalack*windowsize +1)):
        frame = str(totalack*windowsize + i)
        print 'sending the frame ..%s'%frame
        s.sendall(frame)
        data = s.recv(4096)
        if data =='True':
            print '%s is ack..'%frame
        else :
            print 'time out! resending again ..'
            break 
        if i ==windowsize or i == totalframe - totalack*windowsize :
            totalack = totalack + 1
        time.sleep(1)
s.close()
        



import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost',8080))
minimum = 0
maximum = 1e4

data = s.recv(4096)
print data
while True :
    mid =int( (minimum + maximum)//2)
    s.sendall(str(mid))
    prediction = s.recv(4096)
    if prediction=="Equal":
        print 'N '+prediction +' ' + str(mid)
        s.close()
        break
    elif prediction=='Greater than':
        print 'N '+prediction + ' ' + str(mid)
        maximum = mid 
    else :
        print 'N ' + prediction + ' ' + str(mid)
        minimum = mid + 1

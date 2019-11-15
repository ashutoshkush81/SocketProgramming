import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('', 8080))

print 'waiting for server to response'

try:
    data = s.recv(4096)
    print data
except:
    print 'server is not responding.. so closing the connection..'
    s.close()
while True:
    try:
        data = str(raw_input("Enter the string .."))
        s.sendall(data)
        data = s.recv(4096)
        print data
        mess = raw_input("do you want to continue(Y/N) : ")
        if mess == 'y' or mess == 'Y':
            continue
        else:
            print 'connection is closing.. by the client'
            s.close()
            break
    except:
        print 'connection is close by the server ..'
        s.close()
        break

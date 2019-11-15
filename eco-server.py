import socket 

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.bind(('',8080))

s.listen(10)

print 'waiting for new connection ..'

while True:
    conn , addr = s.accept()
    print 'Connection is estb. with addr :(%s , %s)'%addr
    conn.sendall("Connection is estb.")
    while True :
        try:
            data = conn.recv(4096)
            data = data[::-1]
            conn.sendall(data)
        except:
            print 'connection is close by the client ..'
            conn.close()
            break
    mess = str(raw_input("Do you want to continue (Y/N) : "))
    if mess =='y' or mess =="Y":
        continue
    else:
        print 'connections is close by the server ..'
        s.close()
        break


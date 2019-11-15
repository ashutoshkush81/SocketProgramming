#Write a program in which client send a data and server send the data in reverse order..

import socket 

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

s.bind(('',1111))

print 'server is waiting for new connection ..'
while True :
    data , addr = s.recvfrom(4096)
    print 'new connection is estb. with addr : (%s , %s)'%addr
    s.sendto('connection is estb.',addr)
    data , addr =s.recvfrom(4096)
    if data =='q' or data =='Q':
        print 'Connection is close by the client'
        s.close()
        break
    data = data[::-1]
    try :
        s.sendto(data,addr)
    except :
        print data
        s.close()
        break
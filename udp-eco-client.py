#Write a program in which client send a data and server send the data in reverse order..

import socket 

s = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)

while True :
    s.sendto('',('',1111))
    data , addr = s.recvfrom(4096)
    print data 
    message = str(raw_input("Enter the str to reverse (Enter q or Q to quit) : "))
    if message=='q' or message =='Q':
        print 'Connection is closing by clint'
        s.sendto(message,addr)
        s.close()
        break
    s.sendto(message,addr)
    data , addr = s.recvfrom(4096)
    print data 
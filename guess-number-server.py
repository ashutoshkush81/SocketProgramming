import socket
import time
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind(('localhost',8080))
s.listen(10)
while True :
    conn,addr = s.accept()
    print 'Connection is estb. by the addr : (%s , %s)'%addr
    number = int(raw_input("Enter you number : "))
    conn.sendall("Guess the number ?")
    while True :
        guess_number = int(conn.recv(4096))
        if guess_number ==number :
            conn.sendall("Equal")
            break
        elif guess_number >  number :
            conn.sendall("Greater than")
        else :
            conn.sendall("Less than")
    mess = raw_input("Do you want to continue?(Y/N) ")
    if mess =='Y' or mess =='y':
        continue
    else:
        s.close()
        break
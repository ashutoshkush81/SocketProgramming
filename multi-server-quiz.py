import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',8080))
s.listen(10)
print 'TCP/Ip connections started..'
server_list =[]
max_client = 3
while True :
    conn , addr = s.accept()
    print 'Connection is estb. with addr :(%s , %s)'%addr
    server_list.append(conn)
    max_client = max_client-1
    if max_client == 0:
        break

while True :
    boolen = False
    question = str(raw_input("Ask you question : "))
    answer = str(raw_input("Enter your answer : "))
    for i in server_list :
        i.sendall(question)
        while True :
            try :
                data = i.recv(4096)
                if data.capitalize() ==answer.capitalize():
                    i.sendall('True')
                    print 'Right answer by the client %s'%i
                    boolen = True
                    break
                else :
                    i.sendall('False')
                    print 'Wrong answer by the client %s'%i
                    break
            except :
                print 'waiting for answer..'
        if boolen :
            break
    mess = str(raw_input("Do you want to ask more question ? (Y?N) "))
    if mess == 'N' or mess =='n':
        for i in server_list:
            i.sendall("Closing")
            i.close()
        s.close()
        break
s.close()
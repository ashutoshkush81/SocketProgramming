import socket 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',8080))
totalquestionask = 0
totalrightanswer = 0
while True :
    data = s.recv(4096)
    if data =='Closing':
        print 'closing the client ..'
        s.close()
        break
    totalquestionask = totalquestionask + 1
    print data
    answer = str(raw_input("Enter your answer : "))
    s.sendall(answer)
    data = s.recv(4096)
    if data =='True':
        totalrightanswer = totalrightanswer + 1
    print 'Your results...'
    print 'Totalquestionask : %s'%totalquestionask
    print 'Totalcorrectanswer : %s'%totalrightanswer
    print ''
s.close()
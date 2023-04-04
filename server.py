#########################################
import socket

s = socket.socket()
print ("Socket successfully created")

port = 55555
s.bind(('', port))
# put the socket into listening mode
s.listen(5)
print ("socket listening at %s" %(port))

# Establish connection with client.
c, addr = s.accept()
print ('Got connection from ',addr )
c.send(('Thank you for the connection, '+ str(addr) + '. Type something on the CLI\n').encode())
while (True):
        data = c.recv(1024)
        c.send(('Received '+ str(data)+"\n").encode())
        if ("stop" in str(data)):
                # Close the connection with the client
                c.send('Closing connection after stop received'.encode())
                c.close()
                break
        print ('Ending test')
#########################################


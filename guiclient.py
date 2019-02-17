from OpenSSL import SSL
import sys, os, select
import socket

dir = os.curdir

def verify_cb(conn, cert, errnum, depth, ok):
    # This obviously has to be updated
    print 'Got certificate: %s' % cert.get_subject()
    return ok

# Initialize context
ctx = SSL.Context(SSL.SSLv23_METHOD)
ctx.set_verify(SSL.VERIFY_PEER, verify_cb) # Demand a certificate
ctx.use_privatekey_file (os.path.join(dir, 'client.pkey'))
ctx.use_certificate_file(os.path.join(dir, 'client.cert'))
ctx.load_verify_locations(os.path.join(dir, 'CA.cert'))

# Set up client
ip = raw_input("Enter server ip: ")
host = ip
port = 8080
s = SSL.Connection(ctx, socket.socket(socket.AF_INET, socket.SOCK_STREAM))
s.connect((host, port))

print("You are connected to the server\n")
while 1:
     data = s.recv(1024).decode('utf-8')
     print('Server: ' + data)
     if(data == "cmdclose"):
        break


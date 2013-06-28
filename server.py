#!/usr/bin/python2.7
import socket

def main():
  sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  sock.bind(("localhost",2013))
  sock.listen(1)
  while(1):
    conn, addr = sock.accept()
    print "user [",addr,"] has connected"
    while 1:
      data = conn.recv(1024)
      if((data!=None) & (len(data)!=0) & (data!="/dc")):
	print data
      else:
	print "user [",addr,"] has disconnected"
	conn.close()
	break

if __name__=="__main__":
  main()

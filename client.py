#!/usr/bin/python2.7
import socket

def main():

  while(1):
    name = raw_input("your nickname: ")
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server,port = raw_input("server:port : ").split(":")
    if((server is '') | (not port.isdigit())):
	print "Error: Please enter valid server and port"
	continue
    try:
      sock.connect((server,int(port)))
      sock.send("NICKNAME:"+name)
    except socket.error, err:
      print ("Could not connect to {}:{}\n{} ".format(server,port,err))
      continue

    while(1):
      data = raw_input("enter message: ")
      sock.send("DATA:"+data)
      if(data == "/dc"):
	print "disconnected from ", server
	sock.close()
	break;
      elif(data == "/exit"):
	sock.close()
	exit(0)

if __name__=="__main__":
  main()

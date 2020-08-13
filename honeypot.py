#!bin/python

import socket
import os
import time
os.system("clear")

ip = input("Enter your ip to start Honeypot: ")
time.sleep(1)
os.system("clear")
print ("[•]Honeypot Started.....")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, 80))
s.listen(3)
try:
    while True:
        client_con,client_addr = s.accept()
        print ("Visiter Found ![{}]".format(client_addr[0]))
        client_con.send(b"<h1>$You Has Been Hacked!!</h1>")
        data = client_con.recv(2048)
        print (data.decode('utf-8'))

except KeyboardInterrupt as g:
    print ("\nHoneypot Stopped!!")
    s.close()

finally:
    s.close()
s.close

if __name__ == "__main__":
    pass

import socket
hostname = socket.gethostname()
print("Host name of system is:",hostname)

ip = socket.gethostbyname(hostname)
print("Ip address of system is:",ip)

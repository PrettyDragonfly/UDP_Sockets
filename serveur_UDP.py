from socket import *
import select

mysocket1 = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
mysocket2 = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)

mysocket1.bind(('', 2000))
mysocket2.bind(('', 2002))

sockets = [mysocket1, mysocket2]
while True:
    readable, writable, errored = select.select(sockets, [], [])

    if mysocket1 in readable:
        (message, client_address) = mysocket1.recvfrom(100)
        mysocket1.sendto(message, (client_address[0], client_address[1] + 1))
    else:
        (message, client_address) = mysocket2.recvfrom(100)
        mysocket2.sendto(message, (client_address[0], client_address[1] + 1))

mysocket1.close()
mysocket2.close()
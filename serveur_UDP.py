from socket import *

mysocket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)

mysocket.bind(('', 2000))

(message, client_address) = mysocket.recvfrom(60)

mysocket.sendto(message, client_address)

mysocket.close()
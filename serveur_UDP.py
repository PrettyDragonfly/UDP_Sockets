from socket import *

mysocket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
mysocket.bind(('', 2000))
(message, adresse_client) = mysocket.recvfrom(60)
mysocket.sendto(message, adresse_client)
mysocket.close()
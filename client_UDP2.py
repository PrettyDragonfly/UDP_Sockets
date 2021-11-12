from socket import *

mysocket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)

sent = mysocket.sendto(b"Hi !",
    ("", 2002))

(resultat, adresse_serveur) = mysocket.recvfrom(100)

print(resultat)

mysocket.close()
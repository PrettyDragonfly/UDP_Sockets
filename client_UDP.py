from socket import *

sockets = {}

for i in range(2000,2021,2):
    sockets[i] = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    sent = sockets[i].sendto(b"Hi !",
                           ("", i))
    sockets[i].bind(('', i+1))
    (resultat, adresse_serveur) = sockets[i].recvfrom(100)
    print("Le serveur a renvoyé : ",resultat," sur le port ",i+1)

for i in range(2000,2021,2):
    sockets[i].close()
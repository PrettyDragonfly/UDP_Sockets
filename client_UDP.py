from socket import *
import time
import sys

sockets = {}

while True:
    for i in range(2000,2021,2):
        # Création des sockets
        try:
            sockets[i] = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        except : sys.exit(1)

        # Envoie des messages au serveur
        try:
            sent = sockets[i].sendto(b"Hi !",
                                   ("", i))
        except:
            print("Erreur lors de l'envoie du message sur le port ",i)

        # Réception des messages du serveur
        try:
            sockets[i].bind(('', i+1))
            (resultat, adresse_serveur) = sockets[i].recvfrom(100)
            print("Le serveur a renvoyé : ",resultat," sur le port ",i+1)
            time.sleep(1)
        except:
            print("Erreur lors de la réception du message sur le port ",i+1)

# Fermeture des sockets
for i in range(2000,2021,2):
    sockets[i].close()
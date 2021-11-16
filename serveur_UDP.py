from socket import *
import select
import sys

sockets = {}

# Création des sockets sur les ports 2000, 2002, ..., 2020
for i in range(2000,2021,2):
    try:
        sockets[i] = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        sockets[i].bind(('', i))
    except:
        sys.exit(1)

while True:
    readable, writable, errored = select.select(sockets.values(), [], [])

    for sock in sockets.values():
        if sock in readable:
            # Récupération du message
            try:
                (message, client_address) = sock.recvfrom(100)
                add, port = sock.getsockname()
                sock.sendto(message, (client_address[0], port+1))
                print("J'ai reçu :", message, " sur le port ", port,
                  " et je l'ai renvoyé sur le port ", port+1)
            except:
                print("Erreur lors de la réception du message")
                continue

            # Renvoie du message
            try:
                sock.sendto(message, (client_address[0], port + 1))
                print("J'ai reçu :", message, " sur le port ", port,
                      " et je l'ai renvoyé sur le port ", port + 1)
            except:
                print("Erreur lors de l'envoie du message sur le port ",port+1)

# Fermeture de toutes les sockets ouvertes
for i in range(2000,2003,2):
    sockets[i].close()
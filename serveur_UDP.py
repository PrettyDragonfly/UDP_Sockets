from socket import *
import select

sockets = {}

for i in range(2000,2021,2):
    print(i)
    sockets[i] = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    sockets[i].bind(('', i))
    print(sockets[i])

while True:
    readable, writable, errored = select.select(sockets.values(), [], [])

    for sock in sockets.values():
        if sock in readable:
            (message, client_address) = sock.recvfrom(100)
            add, port = sock.getsockname()
            sock.sendto(message, (client_address[0], port+1))
            print("J'ai reçu :", message, " sur le port ", port,
                  " et je l'ai renvoyé sur le port ", port+1)

for i in range(2000,2003,2):
    sockets[i].close()
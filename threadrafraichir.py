import threading
from tool import *

# 1 thread s'éxécute en continue avec le client pour permettre de détecter tout changement (sans bloquer le programme) sur le document et effectuer ainsi le refresh sur la vue client
class RafraichirClientThread(threading.Thread):
    def __init__(self, sock, document):
        threading.Thread.__init__(self)
        self.sock = sock
        self.document = document
        print("=> Nouveau thread suiveur " + self.document)

    def run(self):
        while True:
            donneesRecues = self.sock.recv(9999999).decode()
            rafraichir = donneesRecues in DATA_SEND
            if rafraichir:
                rafraichirClient(self.document)

import threading
from tool import *
import os

# 1 thread s'éxécute en continue avec le client pour permettre de détecter tout changement (sans bloquer le programme) sur le document et effectuer ainsi le refresh sur la vue client
class RafraichirClientThread(threading.Thread):
    def __init__(self, sock, document):
        threading.Thread.__init__(self)
        self.sock = sock
        self.document = document
        self._stop = threading.Event()
        print("=> Vous allez travailler sur " + self.document)

    def run(self):
        stop=False
        while (True and (stop==False)):
            donneesRecues = self.sock.recv(9999999).decode()
            rafraichir = donneesRecues in DATA_SEND
            stop = donneesRecues in SERVER_QUIT
            if rafraichir:
                rafraichirClient(self.document)
            if stop:
                print("***STOP TEST***")
                os.system('exit')
                os.system('exit')
                self.stop()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

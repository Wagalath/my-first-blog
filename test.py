import sys
import signal

def fermeture(signal, frame):
    print('au dodo')
    sys.exit(0)

signal.signal(signal.SIGINT, fermeture)

print('le programme va boucler')
while True:
      print ('boucle')

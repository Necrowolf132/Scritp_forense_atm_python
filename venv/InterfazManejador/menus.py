from io import open
from sys import platform

class Interfaz_menu:

    def __init__(self):
        self.cartel = open('./InterfazManejador/LogoCyttek.txt', 'r')
        print ( self.cartel.read());
        Sistem = platform
        print ('\n                    Bienvenido\n')
        print ('\nUsted actualmente se encuntra corriendo en un sistema {}\n'.format(Sistem))


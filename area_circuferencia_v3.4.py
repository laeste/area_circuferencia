from math import pi
import sys

def circulo(raio):
   return pi * float(raio) ** 2


if __name__ == '__main__':
   if len(sys.argv) < 2:
      print ("E nessecario informa o raio do circulo"
   else:raio = sys.argv[1]
        area = circulo(raio)

    print('area do circulo', area)

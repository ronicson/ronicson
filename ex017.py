'''ca = float(input('Digite o comprimento do cateto adjacente:'))
co = float(input('Digite o comprimento do cateto oposto:'))
hipo = (ca**2 + co**2) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(hipo))'''
import math
ca = float(input('Digite o comprimento do cateto adjacente:'))
co = float(input('Digite o comprimento do cateto oposto:'))
hipo = math.hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hipo))


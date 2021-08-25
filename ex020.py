import random
a1 = input('Digite se nome:')
a2 = input('Digite seu nome:')
a3 = input('Digite seu nome:')
a4 = input('Digite seu nome:')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem dos trabalos sera assim {}'.format(lista))

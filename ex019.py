import random
print('SORTEADOR')
a = input('Digite seu nome:')
b = input('Digite seu nome:')
c = input('Digite seu nome:')
d = input('Digite seu nome:')
lista = [a, b, c, d]
escolhido = random.choice(lista)
print('O aluno escolido foi {}'.format(escolhido))
from math import radians, sin, cos, tan
an = float(input('Digite o angulo que voce deseja:'))
seno = sin(radians(an))
print('O angulo {} tem o SENO de {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O angulo {} tem COSSENO {:.2f}'.format(an, cosseno))
tangente = tan(radians(an))
print('O angulo de {} tem a TANGENTE {:.2f}'.format(an, tangente))

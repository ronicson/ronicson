'''num = float(input('Digite um numero qualquer:'))
print('o numero {} tem parte inteira {}'.format(num, int(num)))'''

import math
num = float(input('Digite um numero qualquer:'))
print('O numero {} tem parte inteira {}'.format(num,math.trunc(num)))

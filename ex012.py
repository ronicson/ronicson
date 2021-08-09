p = float(input('Digite o valor do produto:R$'))
vd = p - (p * 5/100)
print('seu desconto é de {:.2f}R$'.format(p - vd))
print('O novo valor é de {}R$'.format(vd))

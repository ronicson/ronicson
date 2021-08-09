km = float(input('Quantos kilometros você percorreu:'))
d = int(input('Quantos dias você permaneceu com o veiculo:'))
p1 = d * 60
p2 = km * 0.15
print('O valor em diárias é de {}R$ de km é de {:.2f}R$ e total de {:.2f}R$'.format(p1, p2, p1 + p2))

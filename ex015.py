km = float(input('Quantos kilometros você percorreu:'))
d = int(input('Quantos dias você permaneceu com o veiculo:'))
p1 = d * 60
p2 = km * 0.15
print('O valor em diárias é de R${} de kms é de R${:.2f} e total de R${:.2f} a pagar.'.format(p1, p2, p1 + p2))

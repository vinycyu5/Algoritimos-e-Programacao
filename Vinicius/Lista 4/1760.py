#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

quant_pessoas = 4
i = 0
p = 0
somai = 0
somap = 0
cont = 0
while i < quant_pessoas and p < quant_pessoas:
    idade = int(input(""))
    somai = somai + idade
    i = i + 1 
    peso = float(input(""))
    somap = somap + peso
    p = p + 1
    if peso > 90:
        cont = cont + 1
    
media = somai / quant_pessoas
print("Qtd pessoas > 90 Kg: {}".format(cont))
print("Idade média: {:.2f}".format(media))
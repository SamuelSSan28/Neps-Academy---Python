valor = int(input())
cont = 0
moedas  = [1,0.5,0.25,0.10,0.05,0.01]
troco = []


valor = valor/100
for i in range(6):
    if(valor%moedas[i] == 0):
        troco.append(int(valor / moedas[i]))
        valor = 0
    else:
        troco.append(int(valor / moedas[i]))
        valor = valor%moedas[i]

for i in range(6):
    cont += troco[i]

print(cont)
for i in range(6):
    print(troco[i])
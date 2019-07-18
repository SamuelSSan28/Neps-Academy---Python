valor = int(input())
sorteio = input().split()

for i in range(valor):
    sorteio[i] = int(sorteio[i])

cont = 0
aux = 0

for i in range(valor):
    if cont < aux:
        cont = aux

    if cont > int(valor / 2):
        break

    aux = 0

    for j in range(i, valor):
        if (sorteio[i] == sorteio[j]):
            aux += 1
        else:
            i = j
            break

print(cont)
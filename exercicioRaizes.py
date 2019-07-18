#exercicioRaizes
import  math

n = int(input())
lista = input().split()

for i in range(n):
    lista[i] = float(lista[i])
    lista[i] = math.sqrt(lista[i])

for i in lista:
    print("{:.4f}".format(i))
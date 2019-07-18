#exercicio soma dos elementos
N = int(input())
lista = input().split()
soma = 0

for i in range(N):
    lista[i] = int(lista[i])

for i in range(N):
    soma = soma + lista[i]

print(soma)
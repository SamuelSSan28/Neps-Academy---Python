#exercicioOrdenação

n = int(input())

L = input().split()

for i in range(n):
    L[i] = int(L[i])

L.sort()

for i in range(n):
    print(L[i],end=" ")

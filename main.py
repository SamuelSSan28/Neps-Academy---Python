''''
n = int(input())
vet = input().split()
aux = []
resp = []

for i in vet:
    aux.append(i)

aux.sort()

for i in range(n):
    if vet[i] != aux[i]:
        resp.append(vet[i])

if len(resp) > 0:
    resp.sort()
    print(len(resp))
    for i in resp:
        print(i,end=" ")
    print(" ")
else:
    print("0")

'''
""" intervalo entre dois números
n = int(input())
n2 = int(input())

maior = max(n,n2)
menor = min(n,n2)

while(menor <= maior):
    print(menor, end=" ")
    menor += 1

"""
p = []
im = []
for i in range(10):
    n  = int(input())
    if(n%2 == 0):
        p.append(n)
    else:
        im.append(n)

for i in p:
    print(i, end=" ")

print("")

for i in im:
    print(i, end=" ")

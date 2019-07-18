n = int(input())
numeros = ['0','1','2','3','4','5','6','7','8','9']
cont = []
vet = []

for i in range(n):
    s = str(input())
    for i in s:
      vet.append(i)

for i in numeros:
    a = vet.count(i)
    cont.append(a)

for i in range(10):
    print("{} - {}".format(numeros[i],cont[i]))
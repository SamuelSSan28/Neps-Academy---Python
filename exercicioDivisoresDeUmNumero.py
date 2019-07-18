n = int(input())
div = []
cont = 0
soma = 0

for i in range(1,n+1):
    if n%i == 0:
        div.append(i)
        cont += 1
        soma += i


print("{} divisor(es):".format(cont),end=" ")
for i in range(cont):
    print(div[i],end=" ")

print("")
print("Soma de divisores = {}".format(soma))

if cont == 2:
    print("Primo")
else:
    print("Nao primo")
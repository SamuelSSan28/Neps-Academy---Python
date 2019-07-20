n,m  = input().split()

m = int(m)
n = int(n)
x = input().split()

soma = 0
aux = -1
resp = 0

for i in x:
    i = int(i)
    if min(i,m-i) >= aux:
        aux =  min(i,m-i)
        soma = min(i,m-i) + soma
    elif max(i , m-i) >= aux:
        aux = max(i, m - i)
        soma = max(i,m-i) + soma
    else:
        soma = -1
        break;


print(soma)
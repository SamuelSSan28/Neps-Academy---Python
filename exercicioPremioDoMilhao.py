#exercicioPremioDoMilhão

n = int(input())
v = 0
total = 0
cont = 0

for i in range(n):
    v = int(input())
    if(total < 1000000):
        total = v + total;
        cont = cont + 1


print(cont)
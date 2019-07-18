n = int(input())
l = 0
c = 0
cont = 0

for i in range(n):
    l, c = input().split()
    l = int(l)
    c = int(c)
    if l > c:
        cont += c

print(cont)

#exercicioLampada

A = False
B = False
n = int(input())
v = input().split()

for i in range(n):
    if v[i] == '1':
        A = not A
    else:
        A = not A
        B = not B

A = int(A)
B = int(B)

print(A)
print(B)
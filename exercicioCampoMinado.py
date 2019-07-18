n = int(input())
campo  = []
ant  = 0
prox = 0

for i in range(n):
    x = int(input())
    campo.append(x+ant)
    ant = x
    if i > 0:
        campo[i-1] += ant


for i in range(n):
    print(campo[i])
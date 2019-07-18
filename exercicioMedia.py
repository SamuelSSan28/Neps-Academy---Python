n1,n2 = input().split()

n1 = float(n1)
n2 = float(n2)

med = (n1+n2)/2

if med >= 7:
    print("Aprovado")
elif med >=4:
    print("Recuperacao")
else:
    print("Reprovado")
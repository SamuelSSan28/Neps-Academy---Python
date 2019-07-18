#exercicioRisadaEngracada

S = input()
vogais = ['a','e','i','o','u']
R = ''

for c in S:
    if c in vogais:
        R += c

#R[::-1} é uma forma em python pra acessar a string ao contrario
#metodo slice
if R == R[::-1]:
    print("S")
else:
    print("N")
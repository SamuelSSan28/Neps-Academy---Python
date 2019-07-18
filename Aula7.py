#Funções

def calculo(x,y):
    resp = x**2 + y**2
    return  resp

resp = calculo(5,4)
print(resp)

print("---------------------")

def calculo3P(x,y):
    resp = x**2 + y**2
    return  resp,x**2,y**2

#Para armazenar somente o 1 valor
resp, *_ = calculo3P(9,6)

#Para armazenar o 1 e 2 valor
resp, x_quadrado, *_ = calculo3P(9,6)

#Para armazenar os 3 valores
resp, x_quadrado, y_quadrado = calculo3P(9,6)


print(resp)
print(x_quadrado)
print(y_quadrado)
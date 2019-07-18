#Ordenação
L = [3,5,4,1,2]

#Formas de ordenar listas
#Para mudar a lista inicial
L  = sorted(L)
#ou
L.sort()
print(L)

print("------------------------")

L = [3,5,4,1,2]
#Para manter a lista inicial igual
R = sorted(L) #cria uma nova lista
print(L)
print(R)

print("------------------------")

#Para ordenar decrescente
L.sort(reverse = True)
print(L)
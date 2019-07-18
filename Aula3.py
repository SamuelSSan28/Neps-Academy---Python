#Criando uma lista (Vetor), porém as listas podem receber elementos de vários tipos ao mesmo tempo
lista = [1, 2, 3, 4, 5.6, "string"]

#Acessar elemento da lista
lista[0] = 10

#Adicionar elemento no final da lista
lista.append(1)

#Remover elemento da lista
del lista[5]

#imprimir lista
print(lista)

#numeros negativos acessam a lista de trás pra frente
print(lista[-1])
#Entrada de Dados

#Para ler valores separados com espaço tem que usar o comando split
A,B = input().split()

#O comando input sempre armazena os valores como string, então para usar como int temos que transforma-lo em int
A = int(A)
B = int(B)

print(A+B)


#Para receber em linhas diferentes pode fazer assim:
A = int(input())
B = int(input())

print(A+B)

A = float(input())
B = float(input())

print(":.2f",A+B)
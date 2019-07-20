def rota(H,P,F,D):
    if D == 1 and F > P and H < P:
        return 1

    if D == -1 and F < P and H > P:
        return 1

    for i in range(max(H,F) - min(H,F)):
        F = F + D

        if F == P:
            return -1

        if F == H:
            return 1

        if D == -1 and F == 0:
            F = 15

        if D == 1 and F == 15:
            F = 0


H,P,F,D= input().split()

H = int(H) # 15 4
P = int(P) # 9  14
F = int(F) # 8  7
D = int(D) # -1 1

if rota(H,P,F,D) == 1:
    print("S")
else:
    print("N")





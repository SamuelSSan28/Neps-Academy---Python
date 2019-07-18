H,P,F,D= input().split()

H = int(H) # 15
P = int(P) # 9
F = int(F) # 8
D = int(D) # -1

x = F - H
y = F - P

if D == 1:
    if x < y:
        print("S")
    else:
        print("N")
else:
    if x > y:
        print("S")
    else:
        print("N")





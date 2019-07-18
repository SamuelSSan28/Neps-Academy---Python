A = int(input())
B = int(input())
C = int(input())

if A < B and A < C:
    print(1)
    if B < C:
        print(2)
        print(3)
    else:
        print(3)
        print(2)
elif  B < A and B < C:
    print(2)
    if A < C:
        print(1)
        print(3)
    else:
        print(3)
        print(1)
else:
    print(3)
    if A < B:
        print(1)
        print(2)
    else:
        print(2)
        print(1)
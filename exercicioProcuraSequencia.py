n = int(input())
L = input().split()
R = ""
for i in range(n):
    if L[i] != " ":
        R += L[i]

print(R.count('100'))
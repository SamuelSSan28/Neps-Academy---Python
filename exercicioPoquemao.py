doces = int(input())
p1 = int(input())
p2 = int(input())
p3 = int(input())

pkm = [p1,p2,p3]
pkm.sort()

if min(pkm) <= doces:
    doces = doces - pkm.pop(0)

if min(pkm) <= doces:
    doces = doces - pkm.pop(0)

if min(pkm) <= doces:
    doces = doces - pkm.pop(0)


print(3-len(pkm))
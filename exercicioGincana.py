def mdc(a, b):
  while b > 0:
    r = a % b
    a, b = b, r
  return a;


n,m = input().split()

n = int(n)
m = int(m)

while mdc(n, m) > 1: m -= 1

print(m)
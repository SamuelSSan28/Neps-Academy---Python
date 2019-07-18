def fatorial(N):
    resp = 1
    if N == 0:
        resp = 1
    else:
        for i in range(N, 1, -1):
            resp *= i

    return resp;

N = int(input())
print(fatorial(N))
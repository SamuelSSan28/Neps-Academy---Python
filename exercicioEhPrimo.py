def eh_primo(x):
    if x < 2:
        return 0
    for i in range(2,x-1):
        if x%i == 0:
            return 0
    return 1

x = int(input())

if eh_primo(x):
    print('S')
else:
    print('N')
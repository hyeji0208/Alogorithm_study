T = int(input())

a = []
for _ in range(T):
    H, W, N = map(int, input().split())

    YY = N % H
    XX = N // H + 1

    if YY == 0:
        YY = H
        XX = N // H

    a.append(YY * 100 + XX)

print(*a, sep='\n')
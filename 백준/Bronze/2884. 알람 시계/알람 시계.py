h, m = map(int, input().split())

H = h
M = m - 45
if M < 0:
    H = H - 1
    M = M + 60
    if H < 0:
        H = 23


print(H, M)
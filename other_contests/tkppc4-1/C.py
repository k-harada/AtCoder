N, X = map(int, input().split())

for M in range(2, 10 + 1):
    R = N
    Y = 0
    i = 0
    while R > 0:
        Y += (R % M) * (10 ** i)
        R = R // M
        i += 1
    if X == Y:
        break

print(M)

N, D = map(int, input().split())

R = N // (2 * D + 1)

if N % (2 * D + 1) != 0:
    R += 1

print(R)

N, L = map(int, input().split())

S = 0
r_abs = 1000
r = 1000

for i in range(N):
    S += i + L
    if abs(i + L) < r_abs:
        r_abs = abs(i + L)
        r = i + L

print(S - r)

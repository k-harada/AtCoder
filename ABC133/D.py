N = int(input())
A_list = list(map(int, input().split()))

# x = A1
S = 0
for i in range(N - 1):
    if i % 2 == 0:
        S -= A_list[i]
    else:
        S += A_list[i]

x = (A_list[-1] - S) // 2

R_list = [0] * N
R_list[0] = x

for i in range(1, N):
    R_list[i] = A_list[i - 1] - R_list[i - 1]

print(" ".join([str(2 * r) for r in R_list]))

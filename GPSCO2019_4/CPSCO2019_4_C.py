
N, D = map(int, input().split())
Rate_list = list(map(int, input().split()))

RS = list(reversed(sorted(Rate_list)))

res = 0

# set highest, then other two
j = 0
for i in range(N-2):
    rate_high = RS[i]
    while j < N - 1:
        if RS[j + 1] >= rate_high - D:
            j += 1
        else:
            break
    if j - i >= 2:
        res += (j - i) * (j - i - 1) // 2
print(res)

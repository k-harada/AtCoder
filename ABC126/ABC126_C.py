N, K = map(int, input().split())

res = 0

left = K
right = N
n = 1

# start
while left > N:
    n *= 2
    if left % 2 == 0:
        left = left // 2
    else:
        left = left // 2 + 1

# print(left, right, n)
while right > 0:
    res += (right - left + 1) / n
    n *= 2
    right = left - 1
    if left % 2 == 0:
        left = left // 2
    else:
        left = left // 2 + 1
    # print(left, right, n)
print(res / N)

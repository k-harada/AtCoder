N, M = map(int, input().split())

a_list = sorted(list(map(int, input().split())))

res = 0
s = 0
while s < M:
    a = a_list.pop()
    s += a
    res += 1

print(res)
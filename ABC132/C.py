N = int(input())
d_list = sorted(list(map(int, input().split())))


r = N // 2
l = r - 1

print(d_list[r] - d_list[l])

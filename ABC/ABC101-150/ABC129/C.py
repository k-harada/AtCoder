N, M = map(int, input().split())
a_dict = dict()
for _ in range(M):
    a = int(input())
    a_dict[a] = 1

LARGE = 10**9 + 7

r_arr = [0]*(N+1)
r_arr[0] = 1
if a_dict.get(1, 0) == 1:
    r_arr[1] = 0
else:
    r_arr[1] = 1

for i in range(2, N+1):
    if a_dict.get(i, 0) == 1:
        pass
    else:
        r_arr[i] = (r_arr[i-1] + r_arr[i-2]) % LARGE

print(r_arr[-1])

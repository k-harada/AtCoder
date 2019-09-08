N = int(input())
a_list = list(map(int, input().split()))
res_list = [0] * N

for i in range(N - 1, -1, -1):
    r = sum(res_list[i::(i + 1)])
    if (r - a_list[i]) % 2 != 0:
        res_list[i] = 1

S = sum(res_list)
print(S)

if S != 0:
    print(" ".join([str(i+1) for i in range(N) if res_list[i] == 1]))

from heapq import heappush, heappop

LARGE = 10 ** 9 + 7

N, M = map(int, input().split())

h = []

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

for i in range(N):
    heappush(h, (A_list[i], "A"))
for i in range(M):
    heappush(h, (B_list[i], "B"))

DP = [1, 0, 0, 0, 0]
DP_old = [1, 0, 0, 0, 0]
v_old = -1

for _ in range(N + M):
    v, s = heappop(h)
    if v > v_old:
        DP_old[0] = DP[0]
        DP_old[1] = DP[1]
        DP_old[2] = DP[2]
        DP_old[3] = DP[3]
        DP_old[4] = DP[4]
        v_old = v
        if s == "B":
            DP[1] = (DP[1] + DP[0]) % LARGE
            DP[4] = (DP[4] + DP[3]) % LARGE
        else:
            DP[3] = (DP[3] + DP[2]) % LARGE
            DP[2] = (DP[2] + DP[1]) % LARGE
    else:
        if s == "B":
            DP[1] = (DP[1] + DP_old[0]) % LARGE
            DP[4] = (DP[4] + DP_old[3]) % LARGE
        else:
            DP[3] = (DP[3] + DP_old[2]) % LARGE
            DP[2] = (DP[2] + DP_old[1]) % LARGE
    # print(DP)

print(DP[4])

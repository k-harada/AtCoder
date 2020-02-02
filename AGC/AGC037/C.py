from heapq import heappush, heappop

N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

res = True
res_cnt = 0

h = []
for i in range(N):
    if B_list[i] > A_list[i]:
        heappush(h, (-B_list[i], i))
    elif B_list[i] < A_list[i]:
        res = False

while len(h) > 0 and res:
    _, i = heappop(h)
    a = B_list[(i - 1) % N]
    c = B_list[(i + 1) % N]

    if B_list[i] > max(a, c):
        k1 = (B_list[i] - A_list[i]) // (a + c)
        k2 = (B_list[i] - max(a, c)) // (a + c)
        k = min(k1, k2+1)
        if k == 0:
            res = False
        res_cnt += k
        B_list[i] -= k * (a + c)
        if B_list[i] > A_list[i]:
            heappush(h, (-B_list[i], i))
    else:
        res = False

if __name__ == "__main__":
    if res:
        print(res_cnt)
    else:
        print(-1)

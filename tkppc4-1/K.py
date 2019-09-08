from heapq import heappop, heappush

N = int(input())
a_list = list(map(int, input().split()))

done = 0
pushed = N - 1
h = []
heappush(h, -a_list[-1])
res = 0

while done < N:
    d = heappop(h)
    done -= d
    res += 1
    for i in range(max(0, N - 1 - done), pushed):
        heappush(h, -a_list[i])
    pushed = max(0, N - 1 - done)

print(res)

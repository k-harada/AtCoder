from collections import defaultdict, deque
N, M = map(int, input().split())
A = [[0] * M for _ in range(N)]
B = [[0] * M for _ in range(N)]
C = [[0] * M for _ in range(N)]

G = defaultdict(lambda: defaultdict(int))
F = defaultdict(lambda: defaultdict(int))

rows = [0] * (N * M + 1)

for i in range(N):
    A_list = list(map(int, input().split()))
    A[i] = A_list
    for a in A_list:
        G[i + 1][N + (a + M - 1) // M] += 1
        G[N + (a + M - 1) // M][i + 1] = 0



# dfs
for t1 in range(M):

    for i in range(1, N + 1):
        G[0][i] = 1
        F[0][i] = 0
        G[N + i][2 * N + 1] = 1
        F[N + i][2 * N + 1] = 0

    for t2 in range(N):
        queue = deque([0])
        searched = [0] * (2 * N + 2)
        searched[0] = 1
        parent = [0] * (2 * N + 2)

        while len(queue) > 0:
            p = queue.pop()
            for q in G[p].keys():
                if (G[p][q] > 0 or F[q][p] > 0) and searched[q] == 0:
                    parent[q] = p
                    searched[q] = 1
                    queue.append(q)
            if searched[2 * N + 1] == 1:
                break
        path = [2 * N + 1]
        while True:
            path.append(parent[path[-1]])
            if path[-1] == 0:
                break

        for i in range(len(path) - 1, 0, -1):
            p, q = path[i], path[i-1]
            if G[p][q] > 0:
                G[p][q] -= 1
                F[p][q] += 1
            elif F[q][p] > 0:
                F[q][p] -= 1
                G[q][p] += 1

    for i in range(1, N + 1):
        ji = 0
        for j in range(N + 1, 2 * N + 1):
            if F[i][j] == 1:
                ji = j
                break

        F[i][ji] -= 1
        for a in A[i - 1]:
            if N + (a + M - 1) // M == ji:
                A[i - 1].remove(a)
                B[i - 1][t1] = a
                break


for j in range(M):
    c_j = list(sorted([B[i][j] for i in range(N)]))
    for i in range(N):
        C[i][j] = c_j[i]

if __name__ == "__main__":
    for i in range(N):
        print(*B[i])
    for i in range(N):
        print(*C[i])

from collections import defaultdict

N, M, K, X, Y = map(int, input().split())

G = defaultdict(dict)

for _ in range(M):
    A, B = map(int, input().split())
    G[A][B] = 1
    G[B][A] = 1

for A in range(1, N + 1):
    G[A][A] = 1

C_list = ['E'] + list(input().split())
D_list = list(map(int, input().split()))


def score(i, j):
    s = C_list[i] + C_list[j]
    if s in ["GC", "CP", "PG"]:
        return X
    elif s in ["GG", "CC", "PP"]:
        return Y
    else:
        return 0


score_new = [-1000000000] * (N + 1)
score_old = [-1000000000] * (N + 1)
score_new[1] = 0

for t in range(K):
    for p in range(1, N + 1):
        score_old[p] = score_new[p]
    for p in range(1, N + 1):
        score_new[p] = max([score_old[q] for q in G[p].keys()]) + score(p, D_list[t])

print(max(score_new))

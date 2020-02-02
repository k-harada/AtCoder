from functools import lru_cache
N = int(input())


@lru_cache(maxsize=1000)
def get_v(i, j, c, r):

    if i < c // 2 <= j:
        return r
    elif j < c // 2:
        return get_v(i, j, c // 2, r + 1)
    else:
        return get_v(i - c // 2, j - c // 2, c - c // 2, r + 1)


for k in range(N - 1):
    print(*[get_v(k, m, N, 1) for m in range(k + 1, N)])


def solve(h, w, a):
    is_prime = [1] * 1000
    is_prime[0] = 0
    is_prime[1] = 0
    for p in range(1000):
        if not is_prime[p]:
            continue
        for q in range(p * p, 1000, p):
            is_prime[q] = 0
    res = 0
    for i in range(h):
        for j in range(w):
            if is_prime[a[i][j]]:
                res += 1
    return res


def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    res = solve(h, w, a)
    print(res)


def test():
    assert solve(2, 2, [[2, 3], [5, 7]]) == 4


if __name__ == "__main__":
    test()
    main()

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solve(n, d):
    if n * (n - 1) // 2 < n * d:
        return ["No"]
    else:
        res = ["Yes"]
        for add in range(1, d + 1):
            g = gcd(n, add)
            for p0 in range(g):
                p = p0
                while True:
                    q = (p + add) % n
                    res.append(f"{p + 1} {q + 1}")
                    if q == p0:
                        break
                    p = q
        return res





def main():
    n, d = map(int, input().split())
    res = solve(n, d)
    for r in res:
        print(r)


def test():
    assert solve(3, 1) == ["Yes", "1 2", "2 3", "3 1"]
    assert solve(4, 2) == ["No"]


if __name__ == "__main__":
    test()
    main()

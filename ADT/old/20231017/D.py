def solve(n, a, b):
    res = []
    res_a = ""
    res_b = ""
    for i in range(n):
        if i % 2 == 0:
            res_a = res_a + "." * b
            res_b = res_b + "#" * b
        else:
            res_a = res_a + "#" * b
            res_b = res_b + "." * b
    for i in range(n):
        if i % 2 == 0:
            for _ in range(a):
                res.append(res_a)
        else:
            for _ in range(a):
                res.append(res_b)
    return res


def main():
    n, a, b = map(int, input().split())
    res = solve(n, a, b)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()

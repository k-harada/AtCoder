from collections import defaultdict


def solve(n, q, tab_list):
    check = defaultdict(int)
    res = []
    for t, a, b in tab_list:
        p, q = min(a, b), max(a, b)
        k = f"{p} {q}"
        v = check[k]
        if t == 1:
            if a < b:
                if v % 2 == 0:
                    check[k] = v + 1
            else:
                if v < 2:
                    check[k] = v + 2
        elif t == 2:
            if a < b:
                if v % 2 == 1:
                    check[k] = v - 1
            else:
                if v >= 2:
                    check[k] = v - 2
        else:
            if v == 3:
                res.append("Yes")
            else:
                res.append("No")
    return res


def main():
    n, q = map(int, input().split())
    tab_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, tab_list)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()

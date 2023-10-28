from itertools import permutations


def solve(n, r, c):
    perm_a = list(permutations(list(range(n)), n))
    perm_b = list(permutations(list(range(n)), n))
    perm_c = list(permutations(list(range(n)), n))
    for pa in perm_a:
        for pb in perm_b:
            for pc in perm_c:
                success = True
                res = [["."] * n for _ in range(n)]
                # print(pa, pb, pc)
                for i, j in enumerate(pa):
                    res[i][j] = "A"
                for i, j in enumerate(pb):
                    if res[i][j] != ".":
                        success = False
                    res[i][j] = "B"
                for i, j in enumerate(pc):
                    if res[i][j] != ".":
                        success = False
                    res[i][j] = "C"
                for i in range(n):
                    for j in range(n):
                        if res[i][j] == ".":
                            continue
                        if res[i][j] == r[i]:
                            break
                        else:
                            success = False
                # print(res)
                for j in range(n):
                    for i in range(n):
                        if res[i][j] == ".":
                            continue
                        if res[i][j] == c[j]:
                            break
                        else:
                            success = False

                if success:
                    # print(res)
                    return ["Yes"] + ["".join([res[i][j] for j in range(n)]) for i in range(n)]

    return ["No"]


def main():
    n = int(input())
    r = input()
    c = input()
    res = solve(n, r, c)
    for r in res:
        print(r)


def test():
    assert solve(5, "ABCBC", "ACAAB") == [
        "Yes",
        "AC..B",
        ".BA.C",
        "C.BA.",
        "BA.C.",
        "..CBA",
    ]
    assert solve(3, "AAA", "BBB") == ["No"]


if __name__ == "__main__":
    # test()
    main()

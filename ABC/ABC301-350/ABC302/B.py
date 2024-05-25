def solve(h, w, s):
    for i0 in range(h):
        for j0 in range(w):
            for add_i in [-1, 0, 1]:
                for add_j in [-1, 0, 1]:
                    if add_i == 0 and add_j == 0:
                        continue
                    r = ""
                    for k in range(5):
                        i = i0 + add_i * k
                        j = j0 + add_j * k
                        if i < 0 or i >= h or j < 0 or j >= w:
                            r = r + "."
                        else:
                            r = r + s[i][j]
                    if r == "snuke":
                        res = []
                        for k in range(5):
                            i = i0 + add_i * k
                            j = j0 + add_j * k
                            res.append(f"{i + 1} {j + 1}")
                        # print(res)
                        return res
    # print("not found")
    return []


def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    res = solve(h, w, s)
    for r in res:
        print(r)


def test():
    assert solve(6, 6, [
        "vgxgpu", "amkxks", "zhkbpp",
        "hykink", "esnuke", "zplvfj"
    ]) == ["5 2", "5 3", "5 4", "5 5", "5 6"]
    assert solve(5, 5, [
        "ezzzz", "zkzzz", "ezuzs", "zzznz", "zzzzs"
    ]) == ["5 5", "4 4", "3 3", "2 2", "1 1"]


def test_large():
    print(solve(100, 100, ["a" * 100 for _ in range(100)]))


if __name__ == "__main__":
    test()
    # test_large()
    main()

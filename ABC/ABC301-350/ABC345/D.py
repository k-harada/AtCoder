from itertools import permutations


def solve(n, h, w, ab_list):
    for p in permutations(list(range(n))):
        for q in range(2 ** n):
            square = [[0] * w for _ in range(h)]
            success = True
            for i in range(n):
                a, b = ab_list[p[i]]
                if (q >> i) & 1:
                    a, b = b, a
                x_i, y_i = -1, -1
                for x in range(h):
                    for y in range(w):
                        if square[x][y] == 0:
                            x_i, y_i = x, y
                            break
                    if x_i >= 0:
                        break
                if x_i < 0:
                    break
                if x_i + a > h or y_i + b > w:
                    success = False
                    break
                for x in range(x_i, x_i + a):
                    for y in range(y_i, y_i + b):
                        square[x][y] += 1
            # print(square)
            if not success:
                continue
            mi = min([min(square[i]) for i in range(h)])
            mx = max([max(square[i]) for i in range(h)])
            # print(mi, mx)
            if mi == 1 and mx == 1:
                return "Yes"
            else:
                continue

    return "No"


def main():
    n, h, w = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, h, w, ab_list)
    print(res)


def test():
    assert solve(5, 5, 5, [(1, 1), (3, 3), (4, 4), (2, 3), (2, 5)]) == "Yes"
    assert solve(1, 1, 2, [(2, 3)]) == "No"
    assert solve(1, 2, 2, [(1, 1)]) == "No"
    assert solve(5, 3, 3, [(1, 1), (2, 2), (2, 2), (2, 2), (2, 2)]) == "No"


def test_large():
    assert solve(10, 10, 10, [
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
        (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
    ]) == "No"


if __name__ == "__main__":
    # test()
    # test_large()
    main()

from itertools import combinations


def solve(h, w, a):
    res = 0
    for c in combinations(range(h + w - 2), w - 1):
        nums = [a[0][0]]
        moves = [0] * (h + w - 2)
        for j in c:
            moves[j] = 1
        x = 0
        y = 0
        for i in range(h + w - 2):
            if moves[i] == 0:
                x += 1
            else:
                y += 1
            nums.append(a[x][y])
        if len(set(nums)) == h + w - 1:
            res += 1
    return res


def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    res = solve(h, w, a)
    print(res)


def test():
    assert solve(3, 3, [[3, 2, 2], [2, 1, 3], [1, 5, 4]]) == 3


if __name__ == "__main__":
    test()
    main()

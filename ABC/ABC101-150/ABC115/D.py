def solve(n, x):
    layers = [0] * (n + 1)
    meats = [0] * (n + 1)
    layers[0] = 1
    meats[0] = 1
    for i in range(n):
        layers[i + 1] = layers[i] * 2 + 3
        meats[i + 1] = meats[i] * 2 + 1
    y = x
    res = 0
    for i in range(n, 0, -1):
        if y == layers[i]:
            # ちょうどレベルiのバーガーを食べ切る
            res += meats[i]
            y = 0
        elif y >= layers[i - 1] + 2:
            # 上側のレベルi - 1バーガーの途中
            res += meats[i - 1] + 1
            y -= layers[i - 1] + 2
        elif y >= 1:
            # 下側のレベルi - 1バーガーの途中
            y -= 1
    if y == 1:
        res += 1
    return res


def main():
    n, x = map(int, input().split())
    res = solve(n, x)
    print(res)


def test():
    assert solve(2, 7) == 4
    assert solve(1, 1) == 0
    assert solve(50, 4321098765432109) == 2160549382716056


if __name__ == "__main__":
    test()
    main()

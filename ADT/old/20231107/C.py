import math


def solve(n, xy_list):
    m_sq = 0
    for i in range(n - 1):
        xi, yi = xy_list[i]
        for j in range(i + 1, n):
            xj, yj = xy_list[j]
            d_sq = (xi - xj) ** 2 + (yi - yj) ** 2
            m_sq = max(m_sq, d_sq)
    res = math.sqrt(m_sq)
    return res


def main():
    n = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, xy_list)
    print(res)


def test():
    assert abs(solve(3, [(0, 0), (0, 1), (1, 1)]) - 1.4142135624) < 0.000001
    assert abs(solve(5, [
        (315, 271), (-2, -621), (-205, -511), (-952, 482), (165, 463)
    ]) - 1455.7159750446) < 0.000001


if __name__ == "__main__":
    test()
    main()

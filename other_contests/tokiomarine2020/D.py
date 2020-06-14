def solve(n, vw_list, q, vl_list):

    return 0


def main():
    n = int(input())
    vw_list = [list(map(int, input().split())) for _ in range(n)]
    q = int(input())
    vl_list = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, vw_list, q, vl_list)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve() == 0
    assert solve() == 0
    assert solve() == 0


if __name__ == "__main__":
    test()
    main()

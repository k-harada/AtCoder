def solve():
    return 0


def main():
    h, w, k = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    
    res = solve()
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

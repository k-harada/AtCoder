def solve(n, a, b, c, d):
    # Xから
    a_ = 0
    b_ = b
    c_ = c
    d_ = d
    st = "X"
    while True:
        if st == "X":
            if b_ > 0:
                st = "Y"
                b_ -= 1
            elif a_ + b_ + c_ + d_ > 0:
                break
        else:
            d_ = 0
            if c_ > 0:
                st = "X"
                c_ -= 1
            elif a_ + b_ + c_ + d_ > 0:
                break
        if a_ + b_ + c_ + d_ == 0:
            return "Yes"
    # Yから
    a_ = a
    b_ = b
    c_ = c
    d_ = 0
    st = "Y"
    while True:
        if st == "X":
            a_ = 0
            if b_ > 0:
                st = "Y"
                b_ -= 1
            elif a_ + b_ + c_ + d_ > 0:
                break
        else:
            if c_ > 0:
                st = "X"
                c_ -= 1
            elif a_ + b_ + c_ + d_ > 0:
                break
        if a_ + b_ + c_ + d_ == 0:
            return "Yes"
    return "No"


def main():
    n, a, b, c, d = map(int, input().split())
    res = solve(n, a, b, c, d)
    print(res)


def test():
    assert solve(5, 1, 1, 1, 1) == "Yes"
    assert solve(5, 1, 2, 1, 0) == "Yes"
    assert solve(5, 0, 4, 0, 0) == "No"


if __name__ == "__main__":
    test()
    main()

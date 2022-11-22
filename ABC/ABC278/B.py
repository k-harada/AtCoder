def solve(h, m):
    h_ = h
    m_ = m

    while True:
        hh = (h_ // 10) * 10 + (m_ // 10)
        mm = (h_ % 10) * 10 + (m_ % 10)
        if 0 <= hh < 24 and 0 <= mm < 59:
            return f"{h_} {m_}"
        m_ += 1
        if m_ == 60:
            m_ = 0
            h_ += 1
        if h_ == 24:
            h_ = 0
        # print(h_, m_)
    return "0 0"


def main():
    h, m = map(int, input().split())
    res = solve(h, m)
    print(res)


def test():
    assert solve(1, 23) == "1 23"
    assert solve(19, 57) == "20 0"
    assert solve(20, 40) == "21 0"


if __name__ == "__main__":
    test()
    main()

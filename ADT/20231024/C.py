def solve(a, b):
    m_a = len(str(a))
    m_b = len(str(b))
    a_add = "0" * max(m_b - m_a, 0) + str(a)
    b_add = "0" * max(m_a - m_b, 0) + str(b)
    for i in range(max(m_a, m_b)):
        if int(a_add[i]) + int(b_add[i]) >= 10:
            return "Hard"
    return "Easy"


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(229, 390) == "Hard"
    assert solve(123456789, 9876543210) == "Easy"


if __name__ == "__main__":
    test()
    main()

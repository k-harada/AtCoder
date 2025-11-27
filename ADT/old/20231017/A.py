def solve(k):
    if k >= 60:
        res = "22:"
    else:
        res = "21:"
    res = res + f"{100 + k % 60}"[1:]
    return res


def main():
    k = int(input())
    res = solve(k)
    print(res)


def test():
    assert solve(63) == "22:03"
    assert solve(45) == "21:45"
    assert solve(100) == "22:40"


if __name__ == "__main__":
    test()
    main()

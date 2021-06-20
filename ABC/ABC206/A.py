def solve(n):
    s = n * 108
    if s < 20600:
        return "Yay!"
    elif s < 20700:
        return "so-so"
    else:
        return ":("


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(180) == "Yay!"
    assert solve(200) == ":("
    assert solve(191) == "so-so"


if __name__ == "__main__":
    test()
    main()

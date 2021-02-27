def solve(a, b):
    res = (1.0 - float(b) / float(a)) * 100
    return res


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


if __name__ == "__main__":
    main()

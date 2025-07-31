def solve(w):
    x = list(range(1, 101)) + list(range(100, 10100, 100)) + list(range(10000, 1010000, 10000))
    s = " ".join([str(a) for a in x])
    return [300, s]


def main():
    w = int(input())
    res = solve(w)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()

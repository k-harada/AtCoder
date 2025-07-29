def solve(n, a, b):
    for i in range(n):
        for j in range(n):
            if a[i][j] != b[i][j]:
                return f"{i + 1} {j + 1}"
    return "0 0"


def main():
    n = int(input())
    a = [input() for _ in range(n)]
    b = [input() for _ in range(n)]
    res = solve(n, a, b)
    print(res)


def test():
    assert solve(3, ["abc", "def", "ghi"], ["abc", "bef", "ghi"]) == "2 1"
    assert solve(1, ["f"], ["q"]) == "1 1"
    assert solve(10, [
        "eixfumagit",
        "vtophbepfe",
        "pxbfgsqcug",
        "ugpugtsxzq",
        "bvfhxyehfk",
        "uqyfwtmglr",
        "jaitenfqiq",
        "acwvufpfvv",
        "jhaddglpva",
        "aacxsyqvoj"
    ], [
        "eixfumagit",
        "vtophbepfe",
        "pxbfgsqcug",
        "ugpugtsxzq",
        "bvfhxyehok",
        "uqyfwtmglr",
        "jaitenfqiq",
        "acwvufpfvv",
        "jhaddglpva",
        "aacxsyqvoj"
    ]) == "5 9"


if __name__ == "__main__":
    test()
    main()

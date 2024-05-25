def solve(n, a_list):
    res = [0] * n
    for i in range(7 * n):
        a = a_list[i]
        res[i // 7] += a
    return " ".join([str(r) for r in res])


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(2, [
        1000, 2000, 3000, 4000, 5000, 6000, 7000, 2000, 3000, 4000, 5000, 6000, 7000, 8000
    ]) == "28000 35000"
    assert solve(3, [
        14159, 26535, 89793, 23846, 26433, 83279, 50288, 41971, 69399, 37510, 58209,
        74944, 59230, 78164, 6286, 20899, 86280, 34825, 34211, 70679, 82148
    ]) == "314333 419427 335328"


if __name__ == "__main__":
    test()
    main()

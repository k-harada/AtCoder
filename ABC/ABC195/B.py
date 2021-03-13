def solve(a, b, w):
    res_a = 10 ** 9
    res_b = 0
    temp_a = w * 1000 // b
    temp_b = w * 1000 // a + 1
    for i in range(temp_a, temp_b + 1):
        if a * i <= w * 1000 <= b * i:
            res_a = min(res_a, i)
            res_b = max(res_b, i)
    if res_b > 0:
        return f'{res_a} {res_b}'
    else:
        return "UNSATISFIABLE"


def main():
    a, b, w = map(int, input().split())
    res = solve(a, b, w)
    print(res)


def test():
    assert solve(100, 200, 2) == "10 20"
    assert solve(120, 150, 2) == "14 16"
    assert solve(300, 333, 1) == "UNSATISFIABLE"


if __name__ == "__main__":
    test()
    main()

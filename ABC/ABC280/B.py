def solve(n, s_list):
    d_list = [s_list[0]]
    for i in range(n - 1):
        d_list.append(s_list[i + 1] - s_list[i])
    return " ".join([str(d) for d in d_list])


def main():
    n = int(input())
    s_list = list(map(int, input().split()))
    res = solve(n, s_list)
    print(res)


def test():
    assert solve(3, [3, 4, 8]) == "3 1 4"
    assert solve(10, [
        314159265, 358979323, 846264338, -327950288, 419716939,
        -937510582, 97494459, 230781640, 628620899, -862803482
    ]) == "314159265 44820058 487285015 -1174214626 747667227 -1357227521 1035005041 133287181 397839259 -1491424381"


if __name__ == "__main__":
    test()
    main()

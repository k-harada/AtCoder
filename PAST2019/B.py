def solve(n, a_list):
    res = []
    for i in range(n - 1):
        if a_list[i + 1] > a_list[i]:
            res.append("up {}".format(a_list[i + 1] - a_list[i]))
        elif a_list[i + 1] < a_list[i]:
            res.append("down {}".format(a_list[i] - a_list[i + 1]))
        else:
            res.append("stay")
    return res


def main():
    n = int(input())
    a_list = [0] * n
    for i in range(n):
        a = int(input())
        a_list[i] = a
    res = solve(n, a_list)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()

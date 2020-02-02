def solve_b(n, a_list, b_list, c_list):

    res = sum(b_list)

    for i in range(n - 1):
        if a_list[i] + 1 == a_list[i + 1]:
            res += c_list[a_list[i] - 1]

    return res


def main():

    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))

    print(solve_b(n, a_list, b_list, c_list))


if __name__ == "__main__":
    main()

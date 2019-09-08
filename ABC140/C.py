def solve_c(n, b_list):

    a_list = [0] * n

    a_list[0] = b_list[0]
    a_list[-1] = b_list[-1]
    for i in range(1, n - 1):
        a_list[i] = min(b_list[i - 1], b_list[i])

    return sum(a_list)


def main():

    n = int(input())
    b_list = list(map(int, input().split()))
    
    print(solve_c(n, b_list))


if __name__ == "__main__":
    main()

def solve(t, case_list):
    res_list = []
    for i in range(t):
        n, a_list = case_list[i]
        if n % 2 == 1:
            res_list.append("Second")
        else:
            a_list_s = list(sorted(a_list, reverse=True))
            special = True
            for j in range(n):
                if j % 2 == 0:
                    if a_list_s[j] != a_list_s[j + 1]:
                        special = False
            if special:
                res_list.append("Second")
            else:
                res_list.append("First")
    return res_list


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        n = int(input())
        a_list = list(map(int, input().split()))
        case_list.append([n, a_list])
    res = solve(t, case_list)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()

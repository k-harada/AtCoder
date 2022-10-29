def solve_f(n, s_list):
    res = 'Yes'
    stage = 0
    s_list_s = sorted(s_list)
    length = len(s_list_s)
    resolved = [0] * length
    resolved[-1] = 1

    for i in range(n):
        parents = [s_list_s[k] for k in range(length) if resolved[k]]
        for j in range(length - 1, -1, -1):
            if parents[-1] > s_list_s[j] and resolved[j] == 0:
                resolved[j] = 1
                _ = parents.pop()
            if len(parents) == 0:
                break
        if len(parents) > 0:
            res = "No"
            break

    return res


def main():
    n = int(input())
    s_list = list(map(int, input().split()))
    print(solve_f(n, s_list))


if __name__ == "__main__":
    main()

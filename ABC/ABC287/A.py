def solve(n, s_list):
    y = 0
    for s in s_list:
        if s == "For":
            y += 1
        else:
            y -= 1
    if y > 0:
        return "Yes"
    else:
        return "No"


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    print(res)


if __name__ == "__main__":
    main()

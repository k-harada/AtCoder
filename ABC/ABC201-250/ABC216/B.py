def solve(n, st_list):
    name_list = [s + "-" + t for s, t in st_list]
    if len(set(name_list)) < n:
        return "Yes"
    else:
        return "No"


def main():
    n = int(input())
    st_list = [tuple(input().split()) for _ in range(n)]
    res = solve(n, st_list)
    print(res)


def test():
    assert solve(3, [("tanaka", "taro"), ("sato", "hanako"), ("tanaka", "taro")]) == "Yes"
    assert solve(3, [("saito", "ichiro"), ("saito", "jiro"), ("saito", "saburo")]) == "No"
    assert solve(4, [("sypdgidop", "bkseq"), ("bajsqz", "hh"), ("ozjekw", "mcybmtt"), ("qfeysvw", "dbo")]) == "No"


if __name__ == "__main__":
    test()
    main()

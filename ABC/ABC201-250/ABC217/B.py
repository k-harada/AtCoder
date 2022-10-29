def solve(s1, s2, s3):
    res_dict = {"ABC": 0, "ARC": 0, "AGC": 0, "AHC": 0}
    res_dict[s1] += 1
    res_dict[s2] += 1
    res_dict[s3] += 1
    for k in res_dict.keys():
        if res_dict[k] == 0:
            return k


def main():
    s1 = input()
    s2 = input()
    s3 = input()
    res = solve(s1, s2, s3)
    print(res)


def test():
    assert solve("ARC", "AGC", "AHC") == "ABC"
    assert solve("AGC", "ABC", "ARC") == "AHC"


if __name__ == "__main__":
    test()
    main()

dat = {
    "tourist": 3858,
    "ksun48": 3679,
    "Benq": 3658,
    "Um_nik": 3648,
    "apiad": 3638,
    "Stonefeang": 3630,
    "ecnerwala": 3613,
    "mnbvmar": 3555,
    "newbiedmy": 3516,
    "semiexp": 3481,
}


def solve(s):
    if s in dat.keys():
        return dat[s]
    return -1


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("tourist") == 3858
    assert solve("semiexp") == 3481


if __name__ == "__main__":
    test()
    main()

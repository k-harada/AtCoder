import numpy as np


def test(n):
    res = []
    a = [str(i) for i in range(1, n + 1)]
    res.append("_".join(a))
    for _ in range(1000):
        i = np.random.choice(n - 1)
        a_2 = a[:i] + a[i + 2:]
        a_3 = a[i:i + 2]
        j = np.random.choice(n - 2)
        a = a_2[:j] + a_3 + a_2[j:]
        res.append("_".join(a))
    return np.unique(res)


if __name__ == "__main__":
    print(test(3))
    print(test(4))
    print(test(5))

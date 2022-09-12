N = 1000000007
R = 998244353
R2 = R * 2
S = pow(R, 2**64 - 1, 2**64)
M = 2 ** 64 - N
X = pow(2**64 % R, R - 2, R)
R_inv = pow(R, N - 2, N)
R_2 = pow(R, 2, N)
N_prime = (- pow(N, R - 2, R)) % R


class F:

    def __init__(self):
        self.v_dict = dict()
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.v_dict[c] = 0
        self.calls = 0

    def reset(self):
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.v_dict[c] = 0

    def mul(self, s, t, u, submit):
        self.calls += 1
        if submit:
            print(f"mul {s} {t} {u}")
        if u.isdigit():
            self.v_dict[s] = (self.v_dict[t] * int(u)) % (2 ** 64)
        else:
            self.v_dict[s] = (self.v_dict[t] * self.v_dict[u]) % (2 ** 64)

    def rem(self, s, t, submit):
        self.calls += 1
        if submit:
            print(f"rem {s} {t}")
        self.v_dict[s] = self.v_dict[t] % R

    def add(self, s, t, u, submit):
        self.calls += 1
        if submit:
            print(f"add {s} {t} {u}")
        if u.isdigit():
            self.v_dict[s] = (self.v_dict[t] + int(u)) % (2 ** 64)
        else:
            self.v_dict[s] = (self.v_dict[t] + self.v_dict[u]) % (2 ** 64)

    def mon(self, s, submit):
        self.rem("T", s, submit)
        self.mul("T", "T", str(N_prime), submit)
        self.rem("T", "T", submit)
        self.mul("T", "T", str(N), submit)
        self.add("T", "T", s, submit)
        self.mul("T", "T", str(S), submit)
        self.mul("P", "P", str(0), submit)
        self.add("P", "T", str(0), submit)
        self.add("P", "P", str(M), submit)
        self.mul("Q", "Q", str(0), submit)
        self.add("Q", "T", str(0), submit)
        self.add("Q", "Q", str(R2), submit)
        self.add("Q", "Q", str(M), submit)
        self.rem("P", "P", submit)
        self.mul("P", "P", str(R - 1), submit)
        self.rem("P", "P", submit)
        self.rem("Q", "Q", submit)
        self.add("R", "P", "Q", submit)
        self.mul("R", "R", str(X), submit)
        self.add("R", "R", str(1), submit)
        self.rem("R", "R", submit)
        self.mul("R", "R", str(2 ** 64 - N), submit)
        self.add(s, "T", "R", submit)

    def set(self, k: str, v: int):
        self.v_dict[k] = v

    def get(self, k: str):
        return self.v_dict[k]

    def run(self, a, b, submit):
        self.set("A", a)
        self.set("B", b)
        self.mul("A", "A", str(R_2), submit)
        self.mul("B", "B", str(R_2), submit)
        self.mon("A", submit)
        self.mon("B", submit)
        self.mul("C", "A", "B", submit)
        self.mon("C", submit)
        self.mon("C", submit)
        c = self.get("C")
        return c

    def test_mon(self, v):
        self.set("A", v)
        self.mon("A", False)
        assert self.get("A") == self.montgomery_greed(v)
        self.reset()

    def test_run(self, a, b):
        c = self.run(a, b, False)
        assert c == self.product_greed(a, b)
        self.reset()

    def submit(self):
        _ = self.run(0, 0, False)
        print(self.calls)
        _ = self.run(0, 0, True)

    @staticmethod
    def montgomery_greed(t):
        return (t * R_inv) % N

    @staticmethod
    def montgomery(t):
        u = (t + ((t * N_prime) % R) * N) // R
        if u >= N:
            u -= N
        return u

    @staticmethod
    def product_greed(a, b):
        return (a * b) % N

    def product(self, a, b):
        a_ = self.montgomery(a * R_2)
        b_ = self.montgomery(b * R_2)
        c = self.montgomery(a_ * b_)
        c = self.montgomery(c)
        return c


f = F()


def test_1():
    for a in range(10000):
        assert f.montgomery_greed(a) == f.montgomery(a)
    for a in range(R, R + 10000):
        assert f.montgomery_greed(a) == f.montgomery(a)


def test_2():
    for a in range(R, R + 100):
        for b in range(R, R + 100):
            assert f.product_greed(a, b) == f.product(a, b)


def test_3():
    D = 1000000000000
    for a in range(0, N * R, D):
        f.test_mon(a)
    for a in range(R, R + 10000):
        f.test_mon(a)


def test_4():
    D1 = 1234
    D2 = 1235
    for a in range(R, N, D1):
        for b in range(R, N, D2):
            f.test_run(a, b)


def test_5():
    D1 = 1234567
    D2 = 7235
    for a in range(0, N, D1):
        for b in range(R, N, D2):
            f.test_run(a, b)


if __name__ == "__main__":
    # test_1()
    # test_2()
    # test_3()
    # test_4()
    # test_5()
    f.submit()

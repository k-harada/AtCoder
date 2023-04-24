class Solver:

    def __init__(self, n):
        self.n = n
        self.left = 1
        self.right = n
        self.mid = (self.left + self.right) // 2
    def query(self):
        if self.left == self.right - 1:
            return f"! {self.left}"
        else:
            return f"? {self.mid}"

    def input(self, ans):
        if ans == 0:
            self.left = self.mid
        else:
            self.right = self.mid
        self.mid = (self.left + self.right) // 2


def main():
    n = int(input())
    solver = Solver(n)
    while True:
        s = solver.query()
        print(s)
        if s[0] == "!":
            break
        a = int(input())
        solver.input(a)


if __name__ == "__main__":
    main()

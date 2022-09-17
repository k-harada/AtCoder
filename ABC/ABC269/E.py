class Solver:

    def __init__(self, n):
        self.n = n
        self.left_i = 1
        self.right_i = n
        self.center_i = (self.left_i + self.right_i) // 2
        self.left_j = 1
        self.right_j = n
        self.center_j = (self.left_j + self.right_j) // 2
        self.solved_i = False
        self.solved_j = False
        self.ans_i = -1
        self.ans_j = -1

    def query(self):
        if not self.solved_i:
            return f"? {self.left_i} {self.center_i} {1} {self.n}"
        elif not self.solved_j:
            return f"? {1} {self.n} {self.left_j} {self.center_j}"
        else:
            return f"! {self.ans_i} {self.ans_j}"

    def input(self, ans):
        if ans == -1:
            return "!"
        elif not self.solved_i:
            if ans == self.center_i - self.left_i + 1:  # filled
                self.left_i = self.center_i + 1
                self.center_i = (self.left_i + self.right_i) // 2
            else:  # not filled
                self.right_i = self.center_i
                self.center_i = (self.left_i + self.right_i) // 2
            if self.left_i == self.right_i:
                self.ans_i = self.left_i
                self.solved_i = True
        elif not self.solved_j:
            if ans == self.center_j - self.left_j + 1:  # filled
                self.left_j = self.center_j + 1
                self.center_j = (self.left_j + self.right_j) // 2
            else:  # not filled
                self.right_j = self.center_j
                self.center_j = (self.left_j + self.right_j) // 2
            if self.left_j == self.right_j:
                self.ans_j = self.left_j
                self.solved_j = True


def main():
    n = int(input())
    solver = Solver(n)
    while True:
        res = solver.query()
        if res[0] == "!":
            print(res)
            break
        print(res)
        ans = int(input())
        solver.input(ans)


if __name__ == "__main__":
    main()


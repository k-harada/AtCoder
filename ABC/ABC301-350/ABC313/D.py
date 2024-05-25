class Solver:

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.step = 0
        self.base_list = [str(i) for i in range(1, k + 2)]
        self.new_base = " ".join([str(i) for i in range(1, k)])
        self.temp = [-1] * (n + 1)

    def query(self):
        if self.step == self.n:
            return "!" + " " + " ".join([str(a) for a in self.temp[1:(self.n + 1)]])
        if self.step < self.k + 1:
            return "?" + " " + " ".join(self.base_list[:self.step] + self.base_list[(self.step + 1):])
        else:
            if len(self.new_base) > 0:
                return "?" + " " + self.new_base + " " + str(self.step + 1)
            else:
                return "?" + " " + str(self.step + 1)

    def input(self, ans):
        self.step += 1
        self.temp[self.step] = ans
        if self.step == self.k + 1:
            s = sum(self.temp[1:(self.k + 1)]) % 2
            if s != self.temp[self.k + 1]:
                for i in range(1, self.k + 2):
                    self.temp[i] = 1 - self.temp[i]
            ones = []
            zeros = []
            for i in range(1, self.k + 2):
                if self.temp[i] == 1:
                    ones.append(i)
                else:
                    zeros.append(i)
            s = sum(self.temp[1:(self.k + 2)]) % 2
            if s == 1:
                self.new_base = " ".join([str(a) for a in ones[:-1] + zeros[:-1]])
            else:
                if len(zeros) > 0:
                    self.new_base = " ".join([str(a) for a in ones + zeros[:-2]])
                else:
                    self.new_base = " ".join([str(a) for a in ones[:-2] + zeros])


def main():
    n, k = map(int, input().split())
    solver = Solver(n, k)

    while True:
        res = solver.query()
        if res[0] == "!":
            print(res)
            break
        print(res)
        ans = int(input())
        if ans == -1:
            break
        solver.input(ans)


if __name__ == "__main__":
    main()

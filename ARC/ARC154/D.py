from collections import deque


class Solver:
    def __init__(self, n):
        self.n = n
        self.one = -1
        self.p1 = 1
        self.q1 = 2
        self.finish = False
        self.ab_list = deque()
        self.a_list = deque()
        self.b_list = deque()
        self.a = None
        self.b = None
        self.collection = deque()

    def query(self):
        if self.a is None:
            self.a = self.a_list.popleft()
        if self.b is None:
            self.b = self.b_list.popleft()
        return self.a, self.one, self.b

    def merge(self, ans):
        if ans == "Yes":
            # a > b
            self.ab_list.append(self.b)
            self.b = None
        else:
            self.ab_list.append(self.a)
            self.a = None
        # one-side left
        if len(self.a_list) == 0 and self.a is None:
            self.ab_list.append(self.b)
            while len(self.b_list) > 0:
                self.ab_list.append(self.b_list.popleft())
        if len(self.b_list) == 0 and self.b is None:
            self.ab_list.append(self.a)
            while len(self.a_list) > 0:
                self.ab_list.append(self.a_list.popleft())
        # end and set next
        if len(self.a_list) == 0 and len(self.b_list) == 0:
            self.a = None
            self.b = None
            self.collection.append(self.ab_list)
            self.ab_list = deque()
            # set next
            if len(self.collection) == 1:
                self.finish = True
            else:
                self.a_list = self.collection.popleft()
                self.b_list = self.collection.popleft()
        # print(self.a_list)
        # print(self.a)
        # print(self.b_list)
        # print(self.b)
        # print(self.ab_list)
        # print(self.collection)

    def find_one(self, ans):
        if ans == "Yes":
            self.p1 = self.q1
        self.q1 += 1
        if self.q1 == self.n + 1:
            self.one = self.p1

    def preprocess(self):
        for i in range(self.n):
            if i + 1 != self.one:
                self.collection.append(deque([i + 1]))
        self.a_list = self.collection.popleft()
        self.b_list = self.collection.popleft()

    def answer(self):
        res = [0] * (self.n + 1)
        res[self.one] = 1
        v_arg_sort = self.collection.popleft()
        v = 2
        while len(v_arg_sort):
            p = v_arg_sort.popleft()
            res[p] = v
            v += 1
        return " ".join(["!"] + [str(v) for v in res[1:]])


def main():
    n = int(input())
    if n >= 3:
        solver = Solver(n)
        while solver.one == -1:
            print(f"? {solver.p1} {solver.p1} {solver.q1}")
            ans = input()
            solver.find_one(ans)
        # print(solver.one)
        solver.preprocess()
        while not solver.finish:
            a, one, b = solver.query()
            print(f"? {a} {one} {b}")
            ans = input()
            solver.merge(ans)
        # print(solver.collection)
        print(solver.answer())
    elif n == 2:
        print("? 1 1 2")
        ans = input()
        if ans == "Yes":
            print("! 2 1")
        else:
            print("! 1 2")
    elif n == 1:
        print("! 1")


if __name__ == "__main__":
    main()

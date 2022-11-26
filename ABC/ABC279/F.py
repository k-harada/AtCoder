import sys


sys.setrecursionlimit(10 ** 6)


class DirectedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    # search
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # unite
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self.par[y] = x

    # check
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


def solve(n, q, op_list):
    uf = DirectedUnionFind(n + 1 + 2 * q)
    live = list(range(n + 1))
    move = list(range(n + 1 + 2 * q))
    new_ball = n + 1
    new_id = n + q + 1
    res_list = []
    for op in op_list:
        if op[0] == 1:
            # xにyを移す
            x, y = op[1], op[2]
            if live[y] == 0:
                pass
            elif live[x] == 0:
                # 新しい番号を生成する
                uf.union(new_id, live[y])
                live[x] = new_id
                move[new_id] = x
                new_id += 1
                live[y] = 0
            else:
                # live[y]の親をlive[x]にする
                uf.union(live[x], live[y])
                live[y] = 0
        elif op[0] == 2:
            x = op[1]
            if live[x] != 0:
                # 新しい箱の親をlive[x]にする
                uf.union(live[x], new_ball)
                new_ball += 1
            else:
                # 新しい箱がxを占拠する
                live[x] = new_ball
                move[new_ball] = x
                new_ball += 1
        else:
            x = op[1]
            p = uf.find(x)
            res_list.append(move[p])

    return res_list


def main():
    n, q = map(int, input().split())
    op_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, op_list)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()

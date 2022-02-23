from typing import List, Dict, Tuple
import numpy as np


species_dict: Dict[int, str] = {
    1: "cow",
    2: "pig",
    3: "rabbit",
    4: "dog",
    5: "cat"
}


class Pet:

    def __init__(self, i: int, x: int, y: int, t: int):
        self.species: str = species_dict[t]
        self.species_int: int = t
        self.pet_id: int = i
        self.x: int = x
        self.y: int = y
        self.is_locked: bool = False

    def move(self, s):
        for c in s:
            if c == 'U':
                self.x -= 1
            elif c == 'D':
                self.x += 1
            elif c == 'L':
                self.y -= 1
            elif c == 'R':
                self.y += 1
            else:
                pass


class Human:

    def __init__(self, i: int, x: int, y: int):
        self.human_id: int = i
        self.x: int = x
        self.y: int = y
        self.is_locked: bool = False
        self.task = "nothing"
        self.target = 30, 30

    def act(self, c):
        if c == 'U':
            self.x -= 1
        elif c == 'D':
            self.x += 1
        elif c == 'L':
            self.y -= 1
        elif c == 'R':
            self.y += 1
        else:
            pass


class Map:

    def __init__(self, m: int):
        self.m = m
        self.data = np.zeros((30, 30), dtype=int)
        self.labyrinth = np.zeros((30, 30), dtype=int)
        self.left_aisle = 0
        self.right_aisle = 29
        self.get_labyrinth(m)
        self.pet_area = np.zeros((30, 30), dtype=int)
        self.labyrinth_assigned = [False] * 10
        self.labyrinth_finished = [False] * 10

    def set_pet(self, p: Pet):
        x = p.x
        y = p.y
        self.pet_area[x, y] = 1
        if x > 0:
            self.pet_area[x - 1, y] = 1
        if x < 29:
            self.pet_area[x + 1, y] = 1
        if y > 0:
            self.pet_area[x, y - 1] = 1
        if y < 29:
            self.pet_area[x, y + 1] = 1

    def reset_pet(self):
        self.pet_area *= 0

    def get_labyrinth(self, m: int):
        if m >= 7:
            self.left_aisle = 2
            self.right_aisle = 26
            self.labyrinth[0:30:3, 1:29:2] = 1
            self.labyrinth[2:30:3, 0:29:4] = 1
            self.labyrinth[:, 29] = self.labyrinth[:, 28]

            self.labyrinth[0, 2:27] = 0
            self.labyrinth[29, 29] = 0

            self.labyrinth[:, 3:6] = self.labyrinth[::-1, 3:6]
            self.labyrinth[:, 11:14] = self.labyrinth[::-1, 11:14]
            self.labyrinth[:, 19:22] = self.labyrinth[::-1, 19:22]

        elif m == 6:
            self.left_aisle = 4
            self.right_aisle = 24
            self.labyrinth[0:30:3, 3:27:2] = 1
            self.labyrinth[2:30:3, 2:27:4] = 1

            self.labyrinth[:, 1] = self.labyrinth[:, 2]
            self.labyrinth[:, 0] = self.labyrinth[:, 2]
            self.labyrinth[:, 29] = self.labyrinth[:, 26]
            self.labyrinth[:, 28] = self.labyrinth[:, 26]
            self.labyrinth[:, 27] = self.labyrinth[:, 26]

            self.labyrinth[0, 4:25] = 0
            self.labyrinth[29, :2] = 0
            self.labyrinth[29, 27:] = 0

            self.labyrinth[:, 9:12] = self.labyrinth[::-1, 9:12]
            self.labyrinth[:, 17:20] = self.labyrinth[::-1, 17:20]

        else:
            self.left_aisle = 6
            self.right_aisle = 22
            self.labyrinth[0:30:3, 5:25:2] = 1
            self.labyrinth[2:30:3, 4:25:4] = 1

            self.labyrinth[:, 3] = self.labyrinth[:, 4]
            self.labyrinth[:, 2] = self.labyrinth[:, 4]
            self.labyrinth[:, 1] = self.labyrinth[:, 4]
            self.labyrinth[:, 0] = self.labyrinth[:, 4]
            self.labyrinth[:, 29] = self.labyrinth[:, 24]
            self.labyrinth[:, 28] = self.labyrinth[:, 24]
            self.labyrinth[:, 27] = self.labyrinth[:, 24]
            self.labyrinth[:, 26] = self.labyrinth[:, 24]
            self.labyrinth[:, 25] = self.labyrinth[:, 24]

            self.labyrinth[0, 6:23] = 0
            self.labyrinth[29, :4] = 0
            self.labyrinth[29, 25:] = 0

            self.labyrinth[:, 11:14] = self.labyrinth[::-1, 11:14]
            self.labyrinth[:, 19:22] = self.labyrinth[::-1, 19:22]


class Solver:

    def __init__(self, n: int, pet_list: List[Tuple[int, int, int]], m: int, human_list: List[Tuple[int, int]]):
        self.n: int = n
        self.m: int = m
        self.pet_list: List[Pet] = []
        self.human_list: List[Human] = []
        self.turn: int = 0
        self.map: Map = Map(m)

        for i in range(n):
            x, y, t = pet_list[i]
            self.pet_list.append(Pet(i, x - 1, y - 1, t))

        for i in range(m):
            x, y = human_list[i]
            self.human_list.append(Human(i, x - 1, y - 1))

    def assign_labyrinth(self, h: Human):
        # 迷宮構築の目標を決める
        if h.task == "nothing":
            # 最も近い未アサインの行にアサイン
            d_min = 100
            i_min = -1
            for i in range(10):
                r = 3 * i + 1
                d = abs(h.x - r)
                if d < d_min and not self.map.labyrinth_assigned[i]:
                    d_min = d
                    i_min = i
            if i_min != -1:
                # アサインできた場合
                self.map.labyrinth_assigned[i_min] = True
                h.task = "move_labyrinth"
                if h.y < 15:
                    h.target = (3 * i_min + 1, 0)
                else:
                    h.target = (3 * i_min + 1, 29)
            else:
                # アサインできなかった場合は未アサインのまま
                pass

        if h.task == "move_labyrinth":
            # 建設のための移動が完了していたら構築が目標になる
            if (h.x, h.y) == h.target:
                h.task = "build_labyrinth"
                h.target = (h.x, 29 - h.y)

        if h.task == "build_labyrinth":
            # 建設が完了していたら目標がなくなる
            if (h.x, h.y) == h.target:
                d_labyrinth_local = (self.map.data - self.map.labyrinth)[h.x - 1: h.x + 2, :].min()
                if d_labyrinth_local >= 0:
                    h.task = "nothing"
                    h.target = (30, 30)
                    # この場合だけはもう一回実行する
                    self.assign_labyrinth(h)

    def run(self, pet_actions: str):
        self.turn += 1

        # ペットを移動させる
        if pet_actions == "":
            s_list = ["."] * self.n
        else:
            s_list = list(pet_actions.split())
        for i in range(self.n):
            s = s_list[i]
            self.pet_list[i].move(s)

        # 壁を作っちゃいけない場所（ペットの場所とその隣）を取得
        self.map.reset_pet()
        for p in self.pet_list:
            self.map.set_pet(p)

        d_labyrinth = (self.map.data - self.map.labyrinth).min()
        action_list = []

        if d_labyrinth < 0:
            # 迷宮が完成していない場合
            for h in self.human_list:
                # 行動目標を決める
                self.assign_labyrinth(h)
                # タスク実行

                # 目標が何もない場合は何もしない
                if h.task == "nothing":
                    # 最初から立ち尽くす事案は発生しない
                    action_list.append(".")

                # 目標が移動の場合
                elif h.task == "move_labyrinth":
                    # 違法な場所に立つことを全力で避ける
                    if h.x % 3 != 1:
                        # 行の違反（これは最初にしか起きない）
                        if h.x < h.target[0]:
                            h.x += 1
                            action_list.append("D")
                        else:
                            h.x -= 1
                            action_list.append("U")

                    elif h.x != h.target[0]:
                        # 行があってない場合
                        if h.target[1] == 0:
                            y_target = self.map.left_aisle
                        else:
                            y_target = self.map.right_aisle
                        # まずは左右を合わせる
                        if h.y < y_target:
                            h.y += 1
                            action_list.append("R")
                        elif h.y > y_target:
                            h.y -= 1
                            action_list.append("L")
                        else:
                            # 上下を合わせる
                            if h.x < h.target[0]:
                                h.x += 1
                                action_list.append("D")
                            elif h.x > h.target[0]:
                                h.x -= 1
                                action_list.append("U")
                            else:
                                # unreachable
                                action_list.append("x")
                    else:
                        # 行があっている
                        if h.y < h.target[1]:
                            h.y += 1
                            action_list.append("R")
                        elif h.y > h.target[1]:
                            h.y -= 1
                            action_list.append("L")
                        else:
                            # unreachable because no need to move
                            action_list.append("x")

                # 目標が建築の場合
                elif h.task == "build_labyrinth":
                    # 上に建築するべきか
                    if self.map.labyrinth[h.x - 1, h.y] == 1 and self.map.data[h.x - 1, h.y] == 0:
                        # 建築可能なら実行、ダメなら待機
                        if self.map.pet_area[h.x - 1, h.y] == 0:
                            action_list.append("u")
                            self.map.data[h.x - 1, h.y] = 1
                        else:
                            action_list.append(".")
                    # 下に建築するべきか
                    elif self.map.labyrinth[h.x + 1, h.y] == 1 and self.map.data[h.x + 1, h.y] == 0:
                        # 建築可能なら実行、ダメなら待機
                        if self.map.pet_area[h.x + 1, h.y] == 0:
                            action_list.append("d")
                            self.map.data[h.x + 1, h.y] = 1
                        else:
                            action_list.append(".")
                    # 建築必要なしまたは済なら移動する
                    else:
                        if h.y < h.target[1]:
                            h.y += 1
                            action_list.append("R")
                        elif h.y > h.target[1]:
                            h.y -= 1
                            action_list.append("L")
                        else:
                            # unreachable because no need to build
                            action_list.append("x")
        else:
            action_list = ["."] * self.m
        print("".join(action_list))

        return None


def main():
    n = int(input())
    pet_list = [tuple(map(int, input().split())) for _ in range(n)]
    m = int(input())
    human_list = [tuple(map(int, input().split())) for _ in range(m)]
    solver = Solver(n, pet_list, m, human_list)
    for t in range(300):
        if t == 0:
            pet_actions = ""
        else:
            pet_actions = input()
        solver.run(pet_actions)


if __name__ == "__main__":
    main()

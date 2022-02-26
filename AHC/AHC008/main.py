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
        self.is_jailed: bool = False

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


class Trap:

    def __init__(self, trap_id: int, trap_map_data: np.array, loss_area: int, closer_point_list: List[Tuple[int, int]]):
        self.trap_id = trap_id
        self.is_open = True
        self.is_built = False
        # 30 * 30のnp.array
        self.trap_map_data = trap_map_data

        # trap発動で失う面積
        self.loss_area = loss_area
        # 閉じるときに必要な人間の位置
        self.closer_point_list = closer_point_list

    def update_is_built(self, map_data):
        if (map_data - self.trap_map_data).min() >= 0:
            self.is_built = True
            print("#", "trap", self.trap_id, "is built")
        return None


class Map:

    def __init__(self, m: int):
        self.m = m
        self.data = np.zeros((30, 30), dtype=int)
        self.labyrinth = np.zeros((30, 30), dtype=int)
        # ペットがいて壁を置いてはいけない領域
        self.pet_area = np.zeros((30, 30), dtype=int)
        # 人間がいる領域
        self.human_area = np.zeros((30, 30), dtype=int)

        self.left_aisle = 0
        self.right_aisle = 29
        self.jailer_position: List[int] = []
        self.labyrinth_assigned: List[bool] = []
        self.jailer_assigned: List[int] = []

        self.jailer_assign_count: List[int] = []

        self.trap_list: List[Trap] = []
        self.trap_indices: np.array = 9999 * np.ones((30, 30), dtype=int)

        self.get_labyrinth(m)

    def add_wall(self, x: int, y: int):
        self.data[x, y] = 1
        for trap in self.trap_list:
            if not trap.is_built:
                trap.update_is_built(self.data)

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

    def set_human(self, h: Human):
        x = h.x
        y = h.y
        self.human_area[x, y] += 1

    def reset_count(self):
        self.pet_area *= 0
        self.human_area *= 0

    def get_labyrinth(self, m: int):
        self.left_aisle = 2
        self.right_aisle = 26
        self.jailer_position = [2, 8, 14, 20, 26]
        self.labyrinth_assigned = [False] * 10
        self.jailer_assigned = [0] * 5

        if m == 5:
            self.jailer_assign_count = [1, 1, 1, 1, 1]
        elif m == 6:
            self.jailer_assign_count = [1, 1, 1, 1, 2]
        elif m == 7:
            self.jailer_assign_count = [1, 1, 1, 2, 2]
        elif m == 8:
            self.jailer_assign_count = [1, 1, 2, 2, 2]
        elif m == 9:
            self.jailer_assign_count = [1, 2, 2, 2, 2]
        elif m == 10:
            self.jailer_assign_count = [2, 2, 2, 2, 2]

        self.labyrinth[2::3, 0::6] = 1
        self.labyrinth[0::3, 1::6] = 1
        self.labyrinth[0::3, 3::6] = 1
        self.labyrinth[2::3, 4::6] = 1
        self.labyrinth[2::3, 5::6] = 1
        self.labyrinth[29, 5::6] = 0

        for i in range(30):
            for j in range(30):
                if i % 3 != 2 and j % 6 == 0:
                    self.trap_indices[i, j] = (j // 6) * 10 + (i // 3)
                if i % 3 == 1 and j % 6 == 1:
                    self.trap_indices[i, j] = (j // 6) * 10 + (i // 3)
                if i % 3 == 1 and j % 6 == 3:
                    self.trap_indices[i, j] = ((j // 6) + 1) * 10 + (i // 3)
                if i % 3 != 2 and j % 6 == 4:
                    self.trap_indices[i, j] = ((j // 6) + 1) * 10 + (i // 3)
                if i % 3 != 2 and j % 6 == 5:
                    self.trap_indices[i, j] = ((j // 6) + 1) * 10 + (i // 3)
                if i == 29 and j % 6 == 5:
                    self.trap_indices[i, j] = ((j // 6) + 1) * 10 + (i // 3)
        # print(self.trap_indices)

        # initialize trap
        for i in range(0, 30, 3):
            for j in range(-3, 30, 6):
                trap_map = self.labyrinth * 0
                trap_map[max(0, i - 1):min(30, i + 3), max(0, j):min(30, j + 5)] = self.labyrinth[max(0, i - 1):min(30, i + 3), max(0, j):min(30, j + 5)]
                trap_id = (i // 3) + 10 * ((j + 6) // 6)
                if j == -3:
                    loss_area = 3
                elif j == 27:
                    loss_area = 5
                else:
                    loss_area = 8
                if i == 27 and j != -3:
                    loss_area += 1
                if j == -3:
                    closer_point_list = [(i + 1, 2)]
                elif j == 27:
                    closer_point_list = [(i + 1, 26)]
                else:
                    closer_point_list = [(i + 1, j - 1), (i + 1, j + 5)]
                self.trap_list.append(Trap(trap_id, trap_map, loss_area, closer_point_list))


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
                h.target = (3 * i_min + 1, 0)
            else:
                # 迷宮作りの仕事がなければ看守になる
                # 終わった順に左からアサイン
                j_target = 4
                for j in range(5):
                    if self.map.jailer_assigned[j] < self.map.jailer_assign_count[j]:
                        j_target = j
                        break
                h.task = "move_jail"
                h.target = (h.x, self.map.jailer_position[j_target])
                self.map.jailer_assigned[j_target] += 1

        if h.task == "move_labyrinth":
            # 建設のための移動が完了していたら構築が目標になる
            if (h.x, h.y) == h.target:
                h.task = "build_labyrinth"
                h.target = (h.x, 29 - h.y)

        if h.task == "move_jail":
            # 建設のための移動が完了していたら捕獲が目標になる
            if (h.x, h.y) == h.target:
                h.task = "capture"
                h.target = (30, 30)

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
        self.map.reset_count()
        for p in self.pet_list:
            self.map.set_pet(p)
        for h in self.human_list:
            self.map.set_human(h)

        # トラップごとにどれだけのペットが入ってるかカウント
        pet_count = [0] * len(self.map.trap_list)
        for p in self.pet_list:
            trap_id = self.map.trap_indices[p.x, p.y]
            if trap_id < 1000:
                pet_count[trap_id] += 1
        # 人が入っていたら0にする
        for h in self.human_list:
            trap_id = self.map.trap_indices[h.x, h.y]
            if trap_id < 1000:
                pet_count[trap_id] = 0

        action_list = ["."] * self.m

        # 全員配置についたか確認
        go_flag = True
        for h in self.human_list:
            if h.task != "capture":
                go_flag = False

        # 捕獲実行
        if go_flag:
            runnable_list = []
            for trap in self.map.trap_list:
                trap_id = trap.trap_id
                runnable = False
                if pet_count[trap_id] > 0 and trap.is_built and trap.is_open:
                    runnable = True
                    points = trap.closer_point_list
                    if len(points) == 2:
                        (left_x, left_y), (right_x, right_y) = points
                        # 人がそこにいるか判定
                        if self.map.human_area[left_x, left_y] == 0 or self.map.human_area[right_x, right_y] == 0:
                            runnable = False
                        # 壁を置いていいか判定
                        if self.map.pet_area[left_x, left_y + 1] > 0 or self.map.pet_area[right_x, right_y - 1] > 0:
                            runnable = False
                    else:
                        h_x, h_y = points[0]
                        # 人がそこにいるか判定
                        if self.map.human_area[h_x, h_y] == 0:
                            runnable = False
                        # 壁を置いていいか判定
                        if h_y < 15:
                            w_y = h_y - 1
                        else:
                            w_y = h_y + 1
                        w_x = h_x

                        if self.map.pet_area[w_x, w_y] > 0:
                            runnable = False

                if runnable:
                    runnable_list.append((trap, pet_count[trap_id], trap.loss_area))

            # ソート
            runnable_list_s = list(sorted(runnable_list, key=lambda x: -x[1] * 100 + trap.loss_area))
            # 捕獲実行
            for trap, _, _ in runnable_list_s:
                points = trap.closer_point_list
                if len(points) == 2:
                    (left_x, left_y), (right_x, right_y) = points
                    left_id = 9999
                    right_id = 9999
                    # humanを走査
                    for id_h, h in enumerate(self.human_list):
                        if (h.x, h.y) == (left_x, left_y) and action_list[id_h] == "." and left_id == 9999:
                            left_id = id_h
                        if (h.x, h.y) == (right_x, right_y) and action_list[id_h] == "." and right_id == 9999:
                            right_id = id_h
                    # みつかったら捕獲実行
                    if left_id < 9999 and right_id < 9999:
                        action_list[left_id] = "r"
                        action_list[right_id] = "l"
                        trap.is_open = False
                        # ペットを捕獲状態にする
                        for p in self.pet_list:
                            p_trap_id = self.map.trap_indices[p.x, p.y]
                            if p_trap_id == trap.trap_id:
                                p.is_jailed = True
                else:
                    h_x, h_y = points[0]
                    closer_id = 9999
                    # humanを走査
                    for id_h, h in enumerate(self.human_list):
                        if (h.x, h.y) == (h_x, h_y) and action_list[id_h] == "." and closer_id == 9999:
                            closer_id = id_h
                    # みつかったら捕獲実行
                    if closer_id < 9999:
                        if h_y < 15:
                            action_list[closer_id] = "l"
                        else:
                            action_list[closer_id] = "r"
                        trap.is_open = False
                        # ペットを捕獲状態にする
                        for p in self.pet_list:
                            p_trap_id = self.map.trap_indices[p.x, p.y]
                            if p_trap_id == trap.trap_id:
                                p.is_jailed = True

        # 捕獲以外のアクション実行
        for id_h, h in enumerate(self.human_list):

            # 既に捕獲実行済の場合はskip
            if action_list[id_h] != ".":
                continue

            # 行動目標を決める
            self.assign_labyrinth(h)
            # タスク実行
            # 目標が何もない場合は何もしない
            if h.task == "nothing":
                # 最初から立ち尽くす事案は発生しない
                action_list[id_h] = "."

            # 目標が移動の場合
            elif h.task == "move_labyrinth" or h.task == "move_jail":
                # 違法な場所に立つことを全力で避ける
                if h.x % 3 != 1:
                    # 行の違反（これは最初にしか起きない）
                    if h.x < h.target[0]:
                        h.x += 1
                        action_list[id_h] = "D"
                    else:
                        h.x -= 1
                        action_list[id_h] = "U"

                elif h.x != h.target[0]:
                    # 行があってない場合
                    if h.target[1] == 0:
                        y_target = self.map.left_aisle
                    else:
                        y_target = self.map.right_aisle
                    # まずは左右を合わせる
                    if h.y < y_target:
                        h.y += 1
                        action_list[id_h] = "R"
                    elif h.y > y_target:
                        h.y -= 1
                        action_list[id_h] = "L"
                    else:
                        # 上下を合わせる
                        if h.x < h.target[0]:
                            h.x += 1
                            action_list[id_h] = "D"
                        elif h.x > h.target[0]:
                            h.x -= 1
                            action_list[id_h] = "U"
                        else:
                            # unreachable
                            action_list[id_h] = "X"
                else:
                    # 行があっている
                    if h.y < h.target[1]:
                        h.y += 1
                        action_list[id_h] = "R"
                    elif h.y > h.target[1]:
                        h.y -= 1
                        action_list[id_h] = "L"
                    else:
                        # unreachable because no need to move
                        action_list[id_h] = "X"

            # 目標が建築の場合
            elif h.task == "build_labyrinth":
                # 上に建築するべきか
                if self.map.labyrinth[h.x - 1, h.y] == 1 and self.map.data[h.x - 1, h.y] == 0:
                    # 建築可能なら実行、ダメなら待機
                    if self.map.pet_area[h.x - 1, h.y] == 0:
                        action_list[id_h] = "u"
                        self.map.add_wall(h.x - 1, h.y)
                    else:
                        action_list[id_h] = "."
                # 下に建築するべきか
                elif self.map.labyrinth[h.x + 1, h.y] == 1 and self.map.data[h.x + 1, h.y] == 0:
                    # 建築可能なら実行、ダメなら待機
                    if self.map.pet_area[h.x + 1, h.y] == 0:
                        action_list[id_h] = "d"
                        self.map.add_wall(h.x + 1, h.y)
                    else:
                        action_list[id_h] = "."
                # 建築必要なしまたは済なら移動する
                else:
                    if h.y < h.target[1]:
                        h.y += 1
                        action_list[id_h] = "R"
                    elif h.y > h.target[1]:
                        h.y -= 1
                        action_list[id_h] = "L"
                    else:
                        # unreachable because no need to build
                        action_list[id_h] = "X"
            # 目標が捕獲の場合
            elif h.task == "capture":
                # 最もマンハッタン距離が近い捕獲されていないペットを検知
                # x方向の距離を加重
                d_min = 10000
                i_min = 100
                for i, p in enumerate(self.pet_list):
                    if p.is_jailed:
                        continue
                    d = 2 * abs(p.x - h.x) + abs(p.y - h.y)
                    if d < d_min:
                        d_min = d
                        i_min = i
                if i_min < 100:
                    target_x = self.pet_list[i_min].x
                    # ポジションにいる場合
                    if h.x % 3 == 1:
                        if target_x < h.x - 1:
                            h.x -= 1
                            action_list[id_h] = "U"
                        elif target_x > h.x + 1:
                            h.x += 1
                            action_list[id_h] = "D"
                        else:
                            action_list[id_h] = "."
                    else:
                        if target_x < h.x:
                            h.x -= 1
                            action_list[id_h] = "U"
                        elif target_x > h.x:
                            h.x += 1
                            action_list[id_h] = "D"
                        else:
                            if h.x % 3 == 0:
                                h.x += 1
                                action_list[id_h] = "D"
                            elif h.x % 3 == 2:
                                h.x -= 1
                                action_list[id_h] = "U"
                            else:
                                # unreachable
                                action_list[id_h] = "X"
                else:
                    # 捕獲完了したら待機
                    action_list[id_h] = "."

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

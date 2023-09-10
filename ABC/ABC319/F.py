from heapq import heappop, heappush
from collections import deque


def solve(n, node_list):
    children = [[] for _ in range(n + 1)]
    max_enemy = 0
    i = 2
    m = 0
    potion_id = [-1] * (n + 1)
    potion_id_rev = []
    potion_power = []
    for p, t, s, g in node_list:
        children[p].append(i)
        if t == 2:
            potion_id[i] = m
            potion_id_rev.append(i)
            potion_power.append(g)
            m += 1
        else:
            max_enemy = max(max_enemy, s)
        i += 1

    power_list = [-1] * (2 ** m)
    power_list[0] = 1
    queue = deque([(0, 0)])
    visited = [[0] * m for _ in range(2 ** m)]

    while len(queue):
        pp, pb = queue.popleft()
        # print(pp, pb, power, power_before)
        if pp == 0:
            power_before = 0
        else:
            power_before = power_list[pb]
        h_enemy = []
        heappush(h_enemy, (0, 0, 1))
        drunk_potion_list = []
        now_potion = -1
        new_potion_list = []
        for i in range(m):
            if (2 ** i) & pb:
                drunk_potion_list.append(potion_id_rev[i])
            elif (2 ** i) & pp:
                now_potion = potion_id_rev[i]
        # print(drunk_potion_list)
        # print(now_potion)
        # tour before
        while len(h_enemy):
            s, g, p = heappop(h_enemy)
            if s > power_before:
                heappush(h_enemy, (s, g, p))
                break
            else:
                for q in children[p]:
                    p_, t, s, g = node_list[q - 2]
                    if t == 1:
                        if s > power_before:
                            heappush(h_enemy, (s, g, q))
                        else:
                            heappush(h_enemy, (0, 0, q))
                    else:
                        if q in drunk_potion_list:
                            heappush(h_enemy, (0, 0, q))
                        elif q == now_potion:
                            heappush(h_enemy, (power_before + 1, 0, q))
                        else:
                            new_potion_list.append(q)
        # new_tour
        if now_potion != -1:
            power = power_before * potion_power[potion_id[now_potion]]
        else:
            power = 1

        while len(h_enemy):
            s, g, p = heappop(h_enemy)
            if s > power:
                break
            else:
                power += g
                for q in children[p]:
                    p_, t, s, g = node_list[q - 2]
                    if t == 1:
                        heappush(h_enemy, (s, g, q))
                    else:
                        if q in drunk_potion_list:
                            heappush(h_enemy, (0, 0, q))
                        elif q == now_potion:
                            heappush(h_enemy, (0, 0, q))
                        else:
                            new_potion_list.append(q)

        # print(power, new_potion_list)
        power_list[pp] = max(power, power_list[pp])
        for po in new_potion_list:
            po_id = potion_id[po]
            if visited[pp][po_id]:
                continue
            else:
                visited[pp][po_id] = 1
                queue.append((pp + 2 ** po_id, pp))

    # print(power_list)
    if power_list[-1] >= max_enemy:
        return "Yes"
    else:
        return "No"


def main():
    n = int(input())
    node_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, node_list)
    print(res)


if __name__ == "__main__":
    main()

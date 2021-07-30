import math


def solve(n, xy_list):

    # center i
    phi_max = 0.0
    for i in range(n):
        angle_list = []
        x0, y0 = xy_list[i]
        for j in range(n):
            if j == i:
                continue
            x, y = xy_list[j]
            angle = 180 * math.atan2(y - y0, x - x0) / math.pi
            angle_list.append(angle)
        angle_list_s = list(sorted(angle_list))
        left = 0
        right = 0
        while right < n - 1:
            if left == right:
                right += 1
                continue
            phi = angle_list_s[right] - angle_list_s[left]
            if phi > 180:
                phi = 360 - phi
                left += 1
            else:
                right += 1
            phi_max = max(phi_max, phi)
            # print(phi_max, phi)

    return phi_max


def main():
    n = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, xy_list)
    print(res)


def test():
    assert abs(solve(3, [(0, 0), (0, 10), (10, 10)]) - 90) < 0.00001
    assert abs(solve(5, [(8, 6), (9, 1), (2, 0), (1, 0), (0, 1)]) - 171.869897645844) < 0.00001
    assert abs(solve(10, [
        (0, 0), (1, 7), (2, 6), (2, 8), (3, 5), (5, 5), (6, 7), (7, 1), (7, 9), (8, 8)
    ]) - 180.0) < 0.00001


if __name__ == "__main__":
    test()
    main()

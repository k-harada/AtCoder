K = int(input())
X, Y = map(int, input().split())
x, y = 0, 0

M = abs(X) + abs(Y)

if M % 2 == 1 and K % 2 == 0:
    r = -1
elif K % 2 == 0:
    if M < K:
        r = 2
    elif M % K == 0:
        r = M // K
    else:
        r = M // K + 1
else:
    if M < K:
        if M % 2 == 0:
            r = 2
        else:
            r = 3
    elif M % K == 0:
        r = M // K
    else:
        r = M // K
        if (M - r) % 2 == 1:
            r += 1
        else:
            r += 2

print(r)


def act(now_x, now_y, target_x, target_y):

    dist = abs(target_x - now_x) + abs(target_y - now_y)
    if target_x - now_x >= 0:
        sign_x = 1
    else:
        sign_x = -1
    if target_y - now_y >= 0:
        sign_y = 1
    else:
        sign_y = -1

    if K % 2 == 0:
        if dist < K:
            if abs(target_x - now_x) >= dist // 2:
                next_x = now_x + sign_x * dist // 2
                next_y = now_y - sign_y * (K - (dist // 2))
            else:
                next_y = now_y + sign_y * dist // 2
                next_x = now_x - sign_x * (K - (dist // 2))
        elif dist % K == 0:
            if abs(target_x - now_x) >= K:
                next_x = now_x + sign_x * K
                next_y = now_y
            else:
                next_y = now_y + sign_y * (K - abs(target_x - now_x))
                next_x = target_x
        else:
            waste_dist = (K - (dist % K)) // 2
            if abs(target_x - now_x) >= dist // 2:
                next_x = now_x + sign_x * (K - waste_dist)
                next_y = now_y - sign_y * waste_dist
            else:
                next_y = now_y + sign_y * (K - waste_dist)
                next_x = now_x - sign_x * waste_dist
    else:
        if dist < K:
            if dist % 2 == 0:
                if abs(target_x - now_x) >= dist // 2:
                    next_x = now_x + sign_x * dist // 2
                    next_y = now_y - sign_y * (K - (dist // 2))
                else:
                    next_y = now_y + sign_y * dist // 2
                    next_x = now_x - sign_x * (K - (dist // 2))
            else:
                next_x = now_x + K
                next_y = now_y
        elif dist % K == 0:
            if abs(target_x - now_x) >= K:
                next_x = now_x + sign_x * K
                next_y = now_y
            else:
                next_y = now_y + sign_y * (K - abs(target_x - now_x))
                next_x = target_x
        else:
            if dist % 2 == 0:
                waste_dist = (K - (dist % K)) // 2
                if abs(target_x - now_x) >= dist // 2:
                    next_x = now_x + sign_x * (K - waste_dist)
                    next_y = now_y - sign_y * waste_dist
                else:
                    next_y = now_y + sign_y * (K - waste_dist)
                    next_x = now_x - sign_x * waste_dist

            else:
                if abs(target_x - now_x) >= K:
                    next_x = now_x + sign_x * K
                    next_y = now_y
                else:
                    next_y = now_y + sign_y * (K - abs(target_x - now_x))
                    next_x = target_x

    # assert abs(next_x - now_x) + abs(next_y - now_y) == K
    return next_x, next_y


if r > 0:
    res_x = [0] * r
    res_y = [0] * r
    for i in range(r):
        x, y = act(x, y, X, Y)
        res_x[i] = x
        res_y[i] = y
    for i in range(r):
        print(str(res_x[i]) + " " + str(res_y[i]))

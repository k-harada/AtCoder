def binary_search(cond, left_initial, right_initial):

    left = left_initial
    right = right_initial

    while left + 1 < right:
        mid = (left + right) // 2

        if cond(mid):
            right = mid
        else:
            left = mid

    return left


def cond(n):
    if n <= k:
        return False
    else:
        return True


if __name__ == "__main__":
    k = 100
    print(binary_search(cond, 0, 177))

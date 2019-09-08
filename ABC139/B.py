def main():
    a, b = map(int, input().split())
    # 1 + R * (A - 1) >= B
    print((b - 1 + a - 2) // (a - 1))


if __name__ == "__main__":
    main()

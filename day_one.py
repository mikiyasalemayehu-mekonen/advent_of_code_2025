def solve():
    password = 0
    start = 50

    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        if not line:
            break

        change = int(line[1:]) % 100

        if line[0] == "R":
            start = (start + change) % 100
        else:
            start = (start - change + 100) % 100
        if start==0:
            password = password + 1

    print(password)


def main():
    solve()


if __name__ == "__main__":
    main()

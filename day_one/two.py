from math import inf

def main():
    password = 0
    pos = 50

    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if not line:
            break

        direction = line[0]
        steps = int(line[1:])

        if direction == 'R':

            crosses = (pos + steps - 1) // 100 - (pos - 1) // 100
            password += crosses
            pos = (pos + steps) % 100

        else:
            crosses = pos // 100 - (pos - steps) // 100
            password += crosses
            pos = (pos - steps) % 100

    print(password)


if __name__ == "__main__":
    main()
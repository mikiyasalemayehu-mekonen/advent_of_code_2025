def solve():
    total = 0

    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if not line:
            break

        digits = list(map(int, line))
        n = len(digits)

        max_two = 0

        for i in range(n):
            tens = digits[i]
            for j in range(i+1, n):
                ones = digits[j]
                num = tens * 10 + ones
                if num > max_two:
                    max_two = num

        total += max_two

    print(total)
solve()
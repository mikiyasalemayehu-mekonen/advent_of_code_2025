def solve():
    K = 12
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

        stack = []
        to_remove = n - K

        for d in digits:
            while stack and to_remove > 0 and stack[-1] < d:
                stack.pop()
                to_remove -= 1
            stack.append(d)


        result_digits = stack[:K]


        num = int("".join(map(str, result_digits)))
        total += num

    print(total)
solve()

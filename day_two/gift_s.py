
import math

ids = input().strip()
ranges = []
for item in ids.split(","):
    a, b = map(int, item.split("-"))
    ranges.append((a, b))
ranges.sort()

global_min = min(a for a, _ in ranges)
global_max = max(b for _, b in ranges)


def in_any_range(x, ranges):
    lo, hi = 0, len(ranges) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        a, b = ranges[mid]
        if a <= x <= b:
            return True
        if x < a:
            hi = mid - 1
        else:
            lo = mid + 1
    return False

min_len = len(str(global_min))
max_len = len(str(global_max))

seen = set()

for L in range(min_len, max_len + 1):

    for d in range(1, L):
        if L % d != 0:
            continue
        repeat = L // d
        if repeat < 2:
            continue


        p_start = 10 ** (d - 1)
        p_end = 10 ** d - 1

        for p in range(p_start, p_end + 1):
            s = str(p) * repeat
            num = int(s)

            if num > global_max:

                break
            if num < global_min:
                continue

            if in_any_range(num, ranges):
                seen.add(num)


print(sum(seen))
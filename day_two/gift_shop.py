ids = input().strip()

ranges = []
for item in ids.split(","):
    start, end = map(int, item.split("-"))
    ranges.append((start, end))

invalid = []

# Collect min/max to know what lengths we need to generate
global_min = min(r[0] for r in ranges)
global_max = max(r[1] for r in ranges)

min_len = len(str(global_min))
max_len = len(str(global_max))

for length in range(2, max_len + 1, 2):
    half_len = length // 2
    half_start = 10**(half_len - 1)
    half_end = 10**half_len - 1

    for half in range(half_start, half_end + 1):
        s_half = str(half)
        candidate = int(s_half + s_half)

        if candidate > global_max:
            break

        for start, end in ranges:
            if start <= candidate <= end:
                invalid.append(candidate)
                break

print(sum(invalid))

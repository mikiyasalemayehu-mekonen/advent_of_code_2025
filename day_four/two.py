def count_neighbors(grid, r, c):
    dirs = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),          (0,1),
        (1,-1),  (1,0),  (1,1)
    ]
    rows, cols = len(grid), len(grid[0])
    cnt = 0
    for dr, dc in dirs:
        rr, cc = r + dr, c + dc
        if 0 <= rr < rows and 0 <= cc < cols:
            if grid[rr][cc] == '@':
                cnt += 1
    return cnt


def simulate(grid):
    removed_total = 0
    rows, cols = len(grid), len(grid[0])
    grid = [list(row) for row in grid]

    while True:
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    if count_neighbors(grid, r, c) < 4:
                        to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = '.'

        removed_total += len(to_remove)

    return removed_total


def main():
    import sys
    grid = [line.strip() for line in sys.stdin if line.strip()]
    print(simulate(grid))


if __name__ == "__main__":
    main()

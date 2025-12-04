def count_accessible(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    total = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            neighbors = 0
            for dr, dc in directions:
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    if grid[rr][cc] == '@':
                        neighbors += 1

            if neighbors < 4:
                total += 1

    return total


def main():
    import sys
    grid = [line.strip() for line in sys.stdin if line.strip()]

    print(count_accessible(grid))


if __name__ == "__main__":
    main()

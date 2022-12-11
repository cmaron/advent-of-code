from functools import reduce


def read_grid(file_name):
    grid = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            grid.append(list(map(int, list(line))))

    return grid


def day8a(file_name):
    grid = read_grid(file_name)
    n = len(grid)
    m = len(grid[0])
    visible = set()
    dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    for i in range(1, n-1):
        for j in range(1, m-1):
            for dx, dy in dirs:
                new_x = i + dx
                new_y = j + dy
                hidden = False
                while not hidden and 0 <= new_x <= n-1 and 0 <= new_y <= m-1:
                    # We need to be taller than the neighbor AND make sure the neighbor is also visible
                    if grid[i][j] <= grid[new_x][new_y]:
                        hidden = True

                    new_x += dx
                    new_y += dy

                if not hidden:
                    visible.add((i, j))

    print(visible)
    print(len(visible) + (2*n) + (2*m) - 4)


def day8b(file_name):
    grid = read_grid(file_name)
    n = len(grid)
    m = len(grid[0])
    dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    max_score = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            scores = []
            for dx, dy in dirs:
                new_x = i + dx
                new_y = j + dy
                curr_score = 0
                while 0 <= new_x <= n-1 and 0 <= new_y <= m-1:
                    curr_score += 1
                    if grid[i][j] <= grid[new_x][new_y]:
                        break
                    new_x += dx
                    new_y += dy

                scores.append(curr_score)

            max_score = max(reduce(lambda x, y: x*y, filter(lambda x: x > 0, scores)), max_score)

    print(max_score)


if __name__ == '__main__':
    day8a('day8.txt')
    day8b('day8.txt')

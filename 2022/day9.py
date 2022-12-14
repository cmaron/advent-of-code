DIRECTIONS = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1)
}


def chebyshev_distance(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def process_tail_update(points):
    for i in range(1, len(points)):
        if chebyshev_distance(points[i-1], points[i]) > 1:
            delta = [min(1, abs(points[i-1][j] - points[i][j])) * (-1 if points[i-1][j] < points[i][j] else 1) for j in range(2)]
            points[i] = (points[i][0]+delta[0], points[i][1]+delta[1])

    return points


def process_file(file_name, length):
    points = [(0, 0) for _ in range(length+1)]
    visited = set()
    visited.add((0, 0))
    with open(file_name) as f:
        for line in f:
            direction, steps = line.strip().split(' ')
            for _ in range(int(steps)):
                points[0] = (points[0][0]+DIRECTIONS[direction][0], points[0][1]+DIRECTIONS[direction][1])
                points = process_tail_update(points)
                visited.add(points[-1])

    print(visited)
    print(len(visited))


def day9a(file_name):
    process_file(file_name, 1)


def day9b(file_name):
    process_file(file_name, 9)


if __name__ == '__main__':
    day9a('day9.txt')
    day9b('day9.small.txt')
    day9b('day9.small.alt.txt')
    day9b('day9.txt')

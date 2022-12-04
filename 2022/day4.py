def process_range_file(file_name, comparator):
    count = 0
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            range_1, range_2 = list(map(lambda x: list(map(int, x.split('-'))), line.split(',')))
            if comparator(range_1, range_2):
                count += 1

    return count


def day4a(file_name):
    print(process_range_file(file_name, lambda x, y:
                             (x[0] <= y[0] and x[1] >= y[1]) or (y[0] <= x[0] and y[1] >= x[1])))


def day4b(file_name):
    print(process_range_file(file_name, lambda x, y: max(x[0], y[0]) <= min(x[1], y[1])))


if __name__ == '__main__':
    day4a('day4.txt')
    day4b('day4.txt')

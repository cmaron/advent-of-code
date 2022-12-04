
def day4a(file_name):
    total_overlaps = 0
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            range_1, range_2 = list(map(lambda x: list(map(int, x.split('-'))), line.split(',')))
            if (range_1[0] <= range_2[0] and range_1[1] >= range_2[1]) or (range_2[0] <= range_1[0] and range_2[1] >= range_1[1]):
                total_overlaps += 1

    print(total_overlaps)


def day4b(file_name):
    overlaps = 0
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            range_1, range_2 = list(map(lambda x: list(map(int, x.split('-'))), line.split(',')))
            if max(range_1[0], range_2[0]) <= min(range_1[1], range_2[1]):
                overlaps += 1

    print(overlaps)


if __name__ == '__main__':
    day4a('day4.txt')
    day4b('day4.txt')

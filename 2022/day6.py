from collections import defaultdict


def process_line(line, distinct_target=4):
    counts = defaultdict(int)

    line = line.strip()
    prev_c = line[0]
    for i, c in enumerate(line):
        counts[c] += 1
        if i > distinct_target-1:
            counts[prev_c] -= 1
            for k, v in list(counts.items()):
                if v <= 0:
                    del counts[k]

            prev_c = line[i - (distinct_target - 1)]

        if len(counts.keys()) == distinct_target:
            print(counts, i + 1)
            return


def day6a(file_name):
    with open(file_name) as f:
        for line in f:
            process_line(line)


def day6b(file_name):
    with open(file_name) as f:
        for line in f:
            process_line(line, 14)


if __name__ == '__main__':
    day6a('day6.txt')
    day6b('day6.txt')

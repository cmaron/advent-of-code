

PRIORITIES = {**{chr(x+97): x+1 for x in range(26)}, **{chr(x+65): x+27 for x in range(26)}}


def day3a(file_name):
    total_score = 0
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            n = len(line)
            left = set(line[0:n//2])
            right = set(line[n//2:])
            total_score += PRIORITIES[left.intersection(right).pop()]

    print(total_score)


def day3b(file_name):
    total_score = 0
    i = 0
    group = []
    with open(file_name) as f:
        for line in f:
            group.append(set(line.strip()))
            i += 1
            if i > 2:
                total_score += PRIORITIES[group[0].intersection(group[1]).intersection(group[2]).pop()]
                i = 0
                group = []

    print(total_score)


if __name__ == '__main__':
    day3a('day3.txt')
    day3b('day3.txt')

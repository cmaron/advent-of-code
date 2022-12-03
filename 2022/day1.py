import heapq


def day1a(file_name):
    curr_max = (0, 0)
    curr_calories = 0
    i = 0
    with open(file_name) as f:
        for line in f:
            l = line.strip()
            if not l:
                if curr_calories > curr_max[0]:
                    curr_max = (curr_calories, i)
                curr_calories = 0
                i += 1
            else:
                curr_calories += int(l)
    print(curr_max)


def day1b(file_name):
    results = []
    curr_calories = 0
    i = 0
    with open(file_name) as f:
        for line in f:
            l = line.strip()
            if not l:
                results.append((curr_calories, i))
                curr_calories = 0
                i += 1
            else:
                curr_calories += int(l)

    heapq.heapify(results)
    total = 0
    for calories, idx in heapq.nlargest(3, results):
        total += calories
        print(calories, idx, total)

    print(total)


if __name__ == '__main__':
    day1a('day1.txt')
    day1b('day1.txt')

from collections import defaultdict, deque


def parse_stack_data(file_name):
    stacks_parsed = False
    stack_lines = []
    stack_index = {}
    stacks = defaultdict(deque)
    with open(file_name) as f:
        for i, line in enumerate(f):
            line = line.rstrip()
            if stacks_parsed:
                return i+1, stacks
            else:
                # If we have hit the label line, actually parse the stack data
                if line[1] == '1':
                    for j, x in enumerate(line):
                        if x != ' ':
                            stack_index[j] = x

                    for stack in stack_lines:
                        for j, c in enumerate(stack):
                            if c not in {' ', '[', ']'}:
                                stacks[stack_index[j]].append(c)

                    stacks_parsed = True
                # The raw stack lines are kept until we hit the label line
                else:
                    stack_lines.append(line)


def parse_move(line):
    data = line.split(' ')
    return {
        'count': int(data[1]),
        'from': data[3],
        'to': data[5],
    }


def process_moves(file_name, move_function):
    move_start, stacks = parse_stack_data(file_name)
    with open(file_name) as f:
        for i, line in enumerate(f):
            line = line.strip()
            if i < move_start:
                pass
            else:
                move_data = parse_move(line)
                move_function(move_data, stacks)

    output = []
    for k in sorted(stacks.keys()):
        output.append(stacks[k][0])
    print(''.join(output))


def day5a(file_name):
    def move_single(move_data, stacks):
        for _ in range(move_data['count']):
            stacks[move_data['to']].appendleft(stacks[move_data['from']].popleft())

    process_moves(file_name, move_single)


def day5b(file_name):
    def move_multiple(move_data, stacks):
        tmp = deque([])
        for _ in range(move_data['count']):
            tmp.appendleft(stacks[move_data['from']].popleft())
        stacks[move_data['to']].extendleft(tmp)

    process_moves(file_name, move_multiple)


if __name__ == '__main__':
    day5a('day5.txt')
    day5b('day5.txt')

from collections import deque


class Node:
    def __init__(self, label: str, size: int, is_dir=False):
        self.label = label
        self.size = size
        self.is_dir = is_dir
        self.children = {}
        self.parent = None

    def add_child(self, label: str, size: int, is_dir=False):
        if label in self.children:
            return

        self.children[label] = Node(label, size, is_dir)
        self.children[label].parent = self

    def update_size(self):
        if not self.is_dir:
            return

        for child in self.children.values():
            child.update_size()
            self.size += child.size

    def __str__(self):
        return '{} ({}, size={})'.format(self.label,
                                         'dir' if self.is_dir else 'file',
                                         self.size)


def parse_command(line: str, context: 'Node') -> 'Node':
    elements = line.split(' ')
    command = elements[1]

    # If we are changing directory, check if it's the parent (..), root (/), or a child directory. For a child directory
    # we create the entry in the tree if we don't have it.
    if command == 'cd':
        directory = elements[2]
        if directory == '..':
            return context.parent

        if directory == '/':
            # Could be sped up by passing around the root directory
            while context.parent:
                context = context.parent
            return context

        if directory not in context.children:
            context.add_child(directory, 0, is_dir=True)

        return context.children[directory]

    else:
        # An ls doesn't change the context
        return context


def parse_entry(line: str, context: 'Node') -> 'Node':
    elements = line.split(' ')

    if elements[0] == 'dir':
        context.add_child(elements[1], 0, is_dir=True)
    else:
        context.add_child(elements[1], int(elements[0]), is_dir=False)
    return context


def create_directory_tree(file_name: str) -> 'Node':
    context = Node('/', 0, is_dir=True)
    root = context
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if line[0] == '$':
                context = parse_command(line, context)
            else:
                context = parse_entry(line, context)

    root.update_size()
    return root


def print_tree(root: 'Node'):
    stack = deque([(root, 1)])
    while stack:
        node, depth = stack.pop()
        print(' ' * (depth-1), '-', str(node))
        for child in node.children.values():
            stack.append((child, depth + 2))


def day6a(file_name):
    root = create_directory_tree(file_name)
    # print_tree(root)

    # find the sum of directories of size at most 100000
    total_sum = 0
    stack = deque([root])
    while stack:
        node = stack.pop()
        if node.is_dir and node.size <= 100000:
            total_sum += node.size
        for child in node.children.values():
            stack.append(child)

    print(total_sum)


def day6b(file_name):
    fs_size = 70000000
    space_needed = 30000000

    root = create_directory_tree(file_name)
    # print_tree(root)

    # Figure out how much space we need to free
    to_free = space_needed - (fs_size - root.size)

    # Traverse the tree and try to find the smallest directory that is >= to_free
    curr_best = root
    stack = deque([root])
    while stack:
        node = stack.pop()
        if node.is_dir and to_free <= node.size < curr_best.size:
            curr_best = node
        for child in node.children.values():
            stack.append(child)

    print(curr_best)


if __name__ == '__main__':
    day6a('day7.txt')
    day6b('day7.txt')

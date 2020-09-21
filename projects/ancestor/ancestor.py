from util import Stack

def earliest_ancestor(ancestors, starting_node):
    s = Stack()
    path = [[starting_node]]
    first = find_ancestors(starting_node, ancestors)

    # edge case: no ancestors
    if len(first) == 0:
        return -1

    s.push(first)
    path.append(first)

    while s.size() > 0:
        cur = s.pop()

        for el in cur:
            nxt = find_ancestors(el, ancestors)
            if len(nxt) > 0:
                s.push(nxt)
                path.append(nxt)

    last = min(path[-1])

    return last


def find_ancestors(child, graph):
    ancestors = []

    for x in graph:
        if x[1] == child:
            ancestors.append(x[0])

    return ancestors






if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                      (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    print(earliest_ancestor(test_ancestors, 2))
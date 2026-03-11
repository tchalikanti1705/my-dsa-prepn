# Simple Python Implementation (Concept)


class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.locked = False
        self.uid = None


def lock(node, uid):
    if node.locked:
        return False

    # check ancestors
    p = node.parent
    while p:
        if p.locked:
            return False
        p = p.parent

    # check descendants
    def check_desc(n):
        for c in n.children:
            if c.locked or check_desc(c):
                return True
        return False

    if check_desc(node):
        return False

    node.locked = True
    node.uid = uid
    return True


def unlock(node, uid):
    if not node.locked or node.uid != uid:
        return False

    node.locked = False
    node.uid = None
    return True

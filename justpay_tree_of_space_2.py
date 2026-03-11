class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        self.isLocked = False
        self.lockedBy = -1
        self.lockedDescendantCount = 0


class Tree:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        node = Node(name)
        self.nodes[name] = node
        return node

    def set_children(self, parent, child):
        parent.children.append(child)
        child.parent = parent

    # LOCK
    def lock(self, name, uid):
        node = self.nodes[name]

        if node.isLocked or node.lockedDescendantCount > 0:
            return False

        # check ancestors
        p = node.parent
        while p:
            if p.isLocked:
                return False
            p = p.parent

        node.isLocked = True
        node.lockedBy = uid

        # update ancestors
        p = node.parent
        while p:
            p.lockedDescendantCount += 1
            p = p.parent

        return True

    # UNLOCK
    def unlock(self, name, uid):
        node = self.nodes[name]

        if not node.isLocked or node.lockedBy != uid:
            return False

        node.isLocked = False
        node.lockedBy = -1

        p = node.parent
        while p:
            p.lockedDescendantCount -= 1
            p = p.parent

        return True

    # collect locked descendants
    def get_locked_descendants(self, node, locked):
        if node.isLocked:
            locked.append(node)

        for child in node.children:
            self.get_locked_descendants(child, locked)

    # UPGRADE
    def upgrade(self, name, uid):
        node = self.nodes[name]

        if node.isLocked or node.lockedDescendantCount == 0:
            return False

        locked_nodes = []
        self.get_locked_descendants(node, locked_nodes)

        # check if all locked by same user
        for n in locked_nodes:
            if n.lockedBy != uid:
                return False

        # unlock all descendants
        for n in locked_nodes:
            self.unlock(n.name, uid)

        # lock current node
        return self.lock(name, uid)


# -----------------------
# Example Usage
# -----------------------

tree = Tree()

# creating nodes
names = ["A", "B", "C", "D", "E", "F"]
for n in names:
    tree.add_node(n)

# building tree
tree.set_children(tree.nodes["A"], tree.nodes["B"])
tree.set_children(tree.nodes["A"], tree.nodes["C"])
tree.set_children(tree.nodes["A"], tree.nodes["D"])
tree.set_children(tree.nodes["B"], tree.nodes["E"])
tree.set_children(tree.nodes["B"], tree.nodes["F"])

# operations
print(tree.lock("E", 1))     # True
print(tree.lock("B", 2))     # False (descendant locked)
print(tree.upgrade("B", 1))  # True
print(tree.lock("E", 1))     # False (ancestor locked)
print(tree.unlock("B", 1))   # True

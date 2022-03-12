class Node:

    def __init__(self, value=None, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        self.diff = 0
        self.height = 1

    def __repr__(self):
        return "<TreeNode val=%s, height=%d diff=%d>" % (self.value, self.height, self.diff)

    def adjust_after_insert(self):
        if self.parent:
            parent = self.parent
            parent.update()
            if parent.diff < -1:
                if self.diff < 0:
                    parent = Node.rotate_to_right(self, parent)
                else:
                    node = Node.rotate_to_left(self.right, self)
                    parent = Node.rotate_to_right(node, parent)
            elif parent.diff > 1:
                if self.diff > 0:
                    parent = Node.rotate_to_left(self, parent)
                else:
                    node = Node.rotate_to_right(self.left, self)
                    parent = Node.rotate_to_left(node, parent)
            return parent.adjust_after_insert()
        else:
            return self

    @classmethod
    def rotate_to_left(cls, node, parent):
        grandparent = parent.parent
        left_child = node.left
        node.parent = grandparent
        if grandparent:
            if grandparent.left is parent:
                grandparent.left = node
            else:
                grandparent.right = node
        parent.right = left_child
        if left_child:
            left_child.parent = parent
        node.left = parent
        parent.parent = node
        parent.update()
        node.update()
        return node

    @classmethod
    def rotate_to_right(cls, node, parent):
        grandparent = parent.parent
        right_child = node.right
        node.parent = grandparent
        if grandparent:
            if grandparent.left is parent:
                grandparent.left = node
            else:
                grandparent.right = node
        parent.left = right_child
        if right_child:
            right_child.parent = parent
        node.right = parent
        parent.parent = node
        parent.update()
        node.update()
        return node

    def update(self):
        left_h, right_h = self.get_left_height(), self.get_right_height()
        self.height = max(left_h, right_h) + 1
        self.diff = right_h - left_h

    def get_left_height(self):
        if not self.left:
            return 0
        return self.left.height

    def get_right_height(self):
        if not self.right:
            return 0
        return self.right.height


class Tree:

    @staticmethod
    def _choose(_x, _y, _z):
        return None

    @staticmethod
    def _action(_x):
        return None

    @staticmethod
    def IN_ORDER(node, action, choose, travel):
        return choose(
            travel(node.left),
            action(node),
            travel(node.right)
        )

    @staticmethod
    def PRE_ORDER(node, action, choose, travel):
        return choose(
            travel(node.left),
            action(node),
            travel(node.right)
        )

    @staticmethod
    def POST_ORDER(node, action, choose, travel):
        return choose(
            travel(node.left),
            action(node),
            travel(node.right)
        )

    @staticmethod
    def BFS(node, action, _choose, _travel):
        queue = [(node, 0)]
        level = 0
        while queue:
            a_node, depth = queue.pop(0)
            if level != depth:
                print()
                level = depth
            action(a_node)
            if a_node.left:
                queue.append((a_node.left, depth+1))
            if a_node.right:
                queue.append((a_node.right, depth+1))
        print("\n")


    @classmethod
    def traveller(cls, action, choose, travel_func):
        action = action or cls._action
        choose = choose or cls._choose
        travel_func = travel_func or cls.IN_ORDER

        def travel(node):
            if node:
                return travel_func(node, action, choose, travel)
        return travel

    @classmethod
    def search_binary_tree(cls, node, value, find_nearest=False):
        if node:
            if node.value == value:
                return node
            is_left = node.value > value
            node_to_search = node.left if is_left else node.right
            if find_nearest and node_to_search is None:
                return node
            return cls.search_binary_tree(node_to_search, value, find_nearest)

    def __init__(self):
        self.root = None

    def insert(self, *values):
        for value in values:
            if not self.root:
                self.root = Node(value)
            else:
                parent = self.search_binary_tree(self.root, value, True)
                node_to_append = Node(value, parent)
                if parent.value > value:
                    parent.left = node_to_append
                elif parent.value < value:
                    parent.right = node_to_append
                self.root = node_to_append.adjust_after_insert()

    def delete(self, value):
        pass

    def search(self, value):
        return self.search_binary_tree(self.root, value)

    def min(self):
        if self.root:
            node = self.root
            while node.left:
                node = node.left
            return node

    def max(self):
        if self.root:
            node = self.root
            while node.right:
                node = node.right
            return node

    def travel(self, action=print, choose=None, travel_func=None):
        action = action if not hasattr(travel_func, "action") else travel_func.action
        Tree.traveller(action, choose, travel_func)(self.root)


if __name__ == "__main__":
    tree = Tree()

    def f():
        tree.travel(action=lambda x: print(x.value, end=" "), travel_func=Tree.BFS)

    for i in range(0,100000):
        tree.insert(i)
        h = tree.root.height

        assert ((i + 2) > 2 ** h /2)








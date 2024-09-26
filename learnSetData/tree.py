# Реализовать бинарное дерево

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_node(self, value):
        if value < self.value:
            if self.left:
                self.left.add_node(value)
            else:
                self.left = Tree(value)
        else:
            if self.right:
                self.right.add_node(value)
            else:
                self.right = Tree(value)

    def __len__(self):
        left_len = len(self.left) if self.left else 0
        right_len = len(self.right) if self.right else 0
        return 1 + left_len + right_len

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()

# Пример использования
tree = Tree(5)
tree.add_node(3)
tree.add_node(8)
tree.add_node(1)
tree.add_node(4)
tree.add_node(6)
tree.add_node(9)
print(len(tree))
tree.print_tree()

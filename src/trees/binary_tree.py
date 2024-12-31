class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def add_left(self, node):
        self.left_child = node
        return self

    def add_right(self, node):
        self.right_child = node
        return self

    def __str__(self):
        left_child_value = self.left_child.value if self.left_child else self.left_child
        right_child_value = self.right_child.value if self.right_child else self.right_child
        return f"{self.value}: {left_child_value} {right_child_value}"

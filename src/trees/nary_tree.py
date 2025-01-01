class NaryNode:

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)
        return self

    def __str__(self):
        return f"{self.value}: {' '.join(child.value for child in self.children)}"
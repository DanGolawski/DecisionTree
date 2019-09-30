class Tree:

    name = None
    nodes = []

    def set_name(self, name):
        self.name = name

    def add_node(self, node):
        self.nodes.append(node)

    def get_name(self):
        return self.name

    def get_nodes(self):
        return self.nodes

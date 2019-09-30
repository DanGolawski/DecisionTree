class Tree:

    name = None
    nodes = {}

    def __init__(self, name, nodes):
        self.name = name
        self.nodes = nodes

    def get_name(self):
        return self.name

    def get_nodes(self):
        return self.nodes

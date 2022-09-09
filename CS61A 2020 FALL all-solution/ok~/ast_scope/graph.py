
class DiGraph:
    def __init__(self):
        self.__adjacency_list = {}

    def add_nodes_from(self, iterable):
        for node in iterable:
            self.add_node(node)

    def add_node(self, node):
        if node not in self.__adjacency_list:
            self.__adjacency_list[node] = set()

    def add_edge(self, source, target):
        self.__adjacency_list[source].add(target)

    def nodes(self):
        return list(self.__adjacency_list)

    def edges(self):
        return list((source, target) for source, targets in self.__adjacency_list.items() for target in targets)

    def neighbors(self, node):
        return list(self.__adjacency_list[node])

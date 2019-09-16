from node import Node


class Statistics:
    def __init__(self, terminal_node: Node, visited_nodes, good_nodes):
        self.terminal_node = terminal_node
        self.visited_nodes = visited_nodes
        self.good_nodes = good_nodes

    def __repr__(self):
        return "Просмотрено вершин: %d\nЛучших вершин: %d\nХороших вершин: %d\nЭффективность алгоритма: " \
               "%.2f%%\nОптимальный путь:\n%s" % (
                   self.visited_nodes_count, self.best_nodes_count, self.good_nodes_count, self.efficiency,
                   self.steps_tree)

    @property
    def optimal_path(self):
        node, path = self.terminal_node, []
        while node:
            path.append(node)
            node = node.parent
        path.reverse()
        return path

    @property
    def visited_nodes_count(self):
        return len(self.visited_nodes)

    @property
    def best_nodes_count(self):
        return len(self.optimal_path)

    @property
    def good_nodes_count(self):
        return len(self.good_nodes)

    @property
    def efficiency(self) -> float:
        return self.best_nodes_count / self.visited_nodes_count * 100

    @property
    def steps_tree(self) -> str:
        steps = ''
        path = self.optimal_path
        return steps.join([str(node) + "\n\n" for node in path])

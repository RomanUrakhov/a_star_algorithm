from node import Node
from queue import PriorityQueue
from statistics import Statistics


def a_star_search(start_sequence, goal_sequence) -> Statistics:
    feasible_solutions = PriorityQueue()
    feasible_solutions.put(Node(start_sequence, goal_sequence), 0)

    visited_nodes = set()
    chosen_nodes = set()
    visited_nodes.add(start_sequence)

    while not feasible_solutions.empty():
        current_node = feasible_solutions.get()
        chosen_nodes.add(current_node)

        if current_node.sequence == goal_sequence:
            stats = Statistics(current_node, visited_nodes, chosen_nodes)
            return stats

        for next_sequence in current_node.neighbours:
            next_node = Node(next_sequence, goal_sequence, parent=current_node)

            if next_sequence not in visited_nodes:
                feasible_solutions.put(next_node, next_node.f)
                visited_nodes.add(next_sequence)

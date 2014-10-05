"""
Project for Module 2. Algorithmic Thinking course, Coursera
20/09/2014
Esther Álvarez Feijoo
"""

from collections import deque
import random


def bfs_visited(graph, start_node):
    """
    BFS-Visited algorithm.

    :param graph: Undirected graph represented as a dictionary
    :param start_node:  Name of starting node in graph
    :return: Set of visited nodes
    """
    visited = set()
    fifo = deque()

    visited.add(start_node)     # add start node to visited and queue
    fifo.append(start_node)

    while len(fifo) != 0:
        target_node = fifo.popleft()
        for neighbor in graph[target_node]:
            if not neighbor in visited:
                visited.add(neighbor)
                fifo.append(neighbor)
    return visited


def cc_visited(graph):
    """
    CC-Visited algorithm.

    :param graph: Undirected graph represented as a dictionary
    :return: list of set of connected components in the graph
    """
    connected_components = list()
    remaining_nodes = set(graph.keys())  # existing nodes in graph
    while len(remaining_nodes) != 0:
        target_node = random.choice(tuple(remaining_nodes))  # random item
        visited = bfs_visited(graph, target_node)
        connected_components.append(visited)
        remaining_nodes = remaining_nodes - visited  # remove visited from remaining_nodes
    return connected_components


def compute_resilience(graph, attack_order):
    """
    Compute the resilience of a graph to a group of attacks.

    :param graph: Undirected graph represented as a dictionary
    :param attack_order: list of nodes to attack, ordered
    :return:  List of largest CC size after every attack. The first entry is filled before any attack.
    """
    result = list()
    result.append(largest_cc_size(graph))  # resilience before attacks
    for attack_target in attack_order:
        attack(graph, attack_target)
        result.append(largest_cc_size(graph))  # resilience before attacks
    return result


def largest_cc_size(graph):
    """
    Obtain the size of largest set of connected components.

    :param graph: Undirected graph as a dictionary
    :return: size of largest set of connected components
    """
    connected_components = cc_visited(graph)  # list of sets of connected components
    largest_size = 0
    for components in connected_components:  # iterate over connected_components
        component_len = len(components)
        if largest_size < component_len:  # store largest size
            largest_size = component_len
    return largest_size


def attack(graph, target_attack):
    """
    Removes a node from the given graph, including its edges

    :param graph: Undirected graph as a dictionary
    :return: Graph
    """
    neighbors = graph.pop(target_attack)  # remove node under attack and recover its neighbors
    for neighbor in neighbors:
        graph[neighbor].remove(target_attack)  # remove its edges, from its neighbors
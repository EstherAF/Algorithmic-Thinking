"""
Project for Module 1. Algorithmic Thinking course, Coursera
03/09/2014
Esther Álvarez Feijoo
"""

def make_complete_graph(num_nodes):
    """
    Creates a complete directed graph with the provided number of nodes,
    and all possible edges, except self-loops
    """
    result_map = {}
    for i_node in range(num_nodes):
        # list of every node, except current
        links = set(range(num_nodes))
        links.remove(i_node)
        # links for this node
        result_map[i_node] = links
    return result_map


def compute_in_degrees(digraph):
    """
    Build a map, with nodes (as keys) and theirs in-degree value (as values)
    """
    result = {}
    # Iterate over each node-key
    for key in digraph:
        if key not in result:
            result[key] = 0
        #Iterate over each edge of node-key
        for edge in digraph[key]:
            if edge in result:
                result[edge] += 1
            else:
                result[edge] = 1
    return result

def in_degree_distribution(digraph):
    """
    Obtain a map, with the distribution (not normalized) of in-degree values
    of the provided node
    """
    in_degree = compute_in_degrees(digraph)
    result = {}
    for node in in_degree:
        value = in_degree[node]
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result
''' __author__ = 'esther.alvarez' '''

EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}

EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}

''' Main function '''


def main():
    print(make_complete_graph(2))
    print(compute_in_degrees(EX_GRAPH1))
    print(in_degree_distribution(EX_GRAPH1))
    return


''' Creates a complete directed graph with the provided number of nodes,
    and all possible edges, except self-loops
'''
def make_complete_graph(num_nodes):
    result_map = {}
    for i_node in range(num_nodes):
        # list of every node, except current
        links = set(range(num_nodes))
        links.remove(i_node)
        # links for this node
        result_map[i_node] = links
    return result_map


''' Build a map, with nodes (as keys) and theirs in-degree value (as values)'''
def compute_in_degrees(digraph):
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


''' Obtain a map, with the distribution (not normalized) of in-degree values
    of the provided node
'''
def in_degree_distribution(digraph):
    in_degree = compute_in_degrees(digraph)
    result = {}
    for node in in_degree:
        value = in_degree[node]
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result
from testing.module1.dataTest import *
from modules.module1 import make_complete_graph, compute_in_degrees, in_degree_distribution


#Execute only when executor is this module
if __name__ == '__main__':

    """
    Main function.
    For testing purposes.
    """
    print(make_complete_graph(2))
    print(compute_in_degrees(EX_GRAPH1))
    print(in_degree_distribution(EX_GRAPH1))
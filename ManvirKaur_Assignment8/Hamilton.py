def dirac(graph):
    """
    Checking to see if the number of neighbors of any node is less than half the number of nodes, because then the graph
    is not Hamiltonian
    
    :param graph: a dictionary of nodes and their neighbors
    :return: True or False
    """
    # Getting the number of nodes in the graph.
    x = len(graph.keys())
    # Iterating through the keys of the dictionary.
    for node in graph.keys():
        # Checking to see if the number of neighbors of any node is less than half the number of nodes
        if len(graph[node]) < x / 2:
            # Returning False if the condition is met.
            return False
    # Returning True if the graph is Hamiltonian.
    return True


def ore(graph):
    """
    If there are two nodes that are not connected, then the sum of the number of nodes connected to each
    of those nodes must be greater than or equal to the total number of nodes in the graph
    
    :param graph: a dictionary where the keys are the nodes and the values are the nodes that the key
    node is connected to
    :return: True or False
    """
    # Getting the number of nodes in the graph.
    x = len(graph.keys())
    # Iterating through the keys of the dictionary.
    for n_node in graph.keys():
        # Iterating through the keys of the dictionary.
        for node_n in graph.keys():
            # Checking to see if the two nodes are not connected.
            if n_node != node_n and node_n not in graph[n_node]:
                # Checking to see if the sum of the number of nodes connected to each of the two nodes is less than
                # the total number of nodes in the graph.
                if len(graph[n_node]) + len(graph[node_n]) < x:
                    # Returning False if the condition is met.
                    return False
    # Returning True if the graph is Hamiltonian.
    return True


# Creating a dictionary where the keys are the nodes and the values are the nodes that the key node is connected to.
G1 = {"a": ["b", "c", "e"], "b": ["a", "c", "e"], "c": ["a", "b", "d", "e"], "d": ["c", "e"], "e": ["a", "b", "c", "d"]}

# Creating a dictionary where the keys are the nodes and the values are the nodes that the key node is connected to.
G2 = {"a": ["b"], "b": ["a", "c" < "d"], "c": ["b", "d"], "d": ["b", "c"], }

# Creating a dictionary where the keys are the nodes and the values are the nodes that the key node is connected to.
G3 = {"a": ["b"], "b": ["a", "c", "g"], "c": ["b", "d", "e"], "d": ["c"], "e": ["c", "f", "g"], "f": ["e"],
      "g": ["b", "e"]}

# Creating a dictionary where the keys are the nodes and the values are the nodes that the key node is connected to.
test = {"a": ["b", "c"], "b": ["a", "c"], "c": ["a", "b", "f"], "d": ["e", "f"], "e": ["d", "f"], "f": ["c", "d", "e"]}

# Creating a list of the graphs that we want to test.
graphs = graphs = [G1, G2, G3, test]
# Creating a list of the names of the graphs that we want to test.
names = ["G1", "G2", "G3", "test"]

# Iterating through the list of graphs and printing the name of the graph, the result of the Dirac's Theorem,
# the result of the Ore's Theorem, and a line to separate the results of each graph.
for i in range(len(graphs)):
    # Printing the name of the graph.
    print("Graph: ", names[i])
    # Printing the name of the theorem, Dirac's Theorem, and the result of the theorem, True or False, for the graph
    # that is being tested.
    print("Dirac's Theorem: ", dirac(graphs[i]))
    # Printing the name of the theorem, Ore's Theorem, and the result of the theorem, True or False, for the graph
    # that is being tested.
    print("Ore's Theorem: ", ore(graphs[i]))
    # Printing a line to separate the results of each graph.
    print("-------------------------------------------------------")
    # Printing a blank line.
    print()

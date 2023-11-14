"""
Author: Manvir Kaur
KUID: 3064194
Date: 12/08/22
Assignment: 08
Purpose: Euler, Hamilton, and Nim
"""

# Importing the random module.
import random


def odds(graph):
    """
    The function returns a list of all the nodes in the graph that have an odd number of edges.
    
    :param graph: a dictionary of nodes and their neighbors
    :return: A list of nodes that have an odd number of edges.
    """
    # Creating an empty list.
    odd = []
    # Iterating through the keys of the dictionary.
    for node in graph:
        # Checking if the number of edges of a node is odd.
        if len(graph[node]) % 2 == 1:
            # Adding the node to the list.
            odd += [node]
    # It returns the list of odd nodes.
    return odd


def Euler_circuit(graph):
    """
    If there are no odd vertices, then there is an Euler circuit
    
    :param graph: a dictionary of the graph
    :return: True or False
    """
    # Checking if the graph has an Euler circuit.
    if len(odds(graph)) == 0:
        # Returning True if the graph has an Euler circuit.
        return True
    # Returning False if the graph doesn't have an Euler circuit.
    else:
        return False


def Euler_path(graph):
    """
    If there are exactly two odd vertices and the graph is not an Euler circuit, then the graph has an
    Euler path
    
    :param graph: a dictionary of lists, where the keys are the nodes and the values are the edges
    :return: True or False
    """
    # Checking if the graph has an Euler path.
    if len(odds(graph)) == 2 and not (Euler_circuit(graph)):
        # Returning True if the graph has an Euler circuit.
        return True
    else:
        # Returning False if the graph doesn't have an Euler circuit.
        return False


def has_edge(graph):
    """
    If any node in the graph has a non-empty list of neighbors, then the graph has an edge
    
    :param graph: the graph, with nodes encoded as strings and edges as lists of strings
    :return: A boolean value.
    """
    # Iterating through the keys of the dictionary.
    for node in graph:
        # Checking if the node has any edges.
        if len(graph[node]) > 0:
            # Returning True if the graph has an Euler circuit.
            return True
    # Returning False if the graph doesn't have an Euler circuit.
    return False


def get_edge(graph: dict):
    """
    It takes a graph and returns a list of all the edges in the graph
    
    :param graph: dict
    :type graph: dict
    :return: A list of tuples.
    """
    # Creating an empty list.
    edges = []
    # Iterating through the keys of the dictionary.
    for node in graph:
        # Iterating through the edges of a node.
        for end in graph[node]:
            # Adding the edge to the list of edges.
            edges.append((node, end))
    # It returns the list of edges.
    return edges


def remove_edge(graph: dict, edge):
    """
    It removes the edge from the graph
    
    :param graph: a dictionary of nodes and their neighbors
    :type graph: dict
    :param edge: a tuple of two vertices
    """
    # It removes the edge from the graph.
    # It removes the edge from the graph.
    graph[edge[0]].remove(edge[1])
    # It removes the edge from the graph.
    graph[edge[1]].remove(edge[0])


def finding_Euler_circuit(graph: dict):
    """
    We start at a random vertex, and then we keep going to the next vertex until we can't go anywhere
    else. 

    If we can't go anywhere else, then we backtrack to the last vertex we visited and try to go
    somewhere else. 
    
    If we can't go anywhere else from there, then we backtrack again. 
    
    We keep doing this until we've visited every vertex. 
    
    If we can't visit every vertex, then there's no Euler circuit. 
    
    If we can visit every vertex, then we've found an Euler circuit
    
    :param graph: dict
    :type graph: dict
    :return: A list of vertices that form an Euler circuit.
    """
    # Creating an empty list.
    visit = []
    # Creating a list of tuples, where each tuple is a key and its value.
    items = list(graph.items())
    # It shuffles the list of tuples.
    random.shuffle(items)
    # Creating a new dictionary with the same keys and values as the original dictionary.
    graph = {k: v[:] for k, v in items}
    # Getting the first key of the dictionary.
    vertex = list(graph.keys())[0]
    # It adds the vertex to the list of vertices.
    visit.append(vertex)

    # Checking if the graph has any edges. If it does, then it iterates through the edges of the
    # graph.
    # If the vertex is in the edge, then it checks if the first vertex of the edge is the same
    # as the vertex.
    # If it is, then it gets the second vertex of the edge. If it isn't, then it gets the
    # first vertex of the edge.
    while has_edge(graph):
        # Iterating through the edges of the graph.
        for edge in get_edge(graph):
            # It checks if the vertex is in the edge.
            if vertex in edge:
                # It checks if the first vertex of the edge is the same as the vertex.
                if edge[0] == vertex:
                    # Getting the second vertex of the edge.
                    vertex = edge[1]
                # Getting the first vertex of the edge.
                else:
                    vertex = edge[0]

                # It removes the edge from the graph.
                remove_edge(graph, edge)
                # It adds the vertex to the list of vertices.
                visit.append(vertex)
                # It breaks the loop.
                break
        else:
            # It returns False if the graph doesn't have an Euler circuit.
            return False
    # It returns the list of vertices that form an Euler circuit.
    return visit


def main():
    """
    It takes a graph as an input and returns a list of nodes that are odd.
    """
    # Creating a dictionary with the nodes and their neighbors.
    G1 = {"a": ["b", "e"], "b": ["a", "e"], "c": ["d", "e"], "d": ["c", "e"], "e": ["a", "b", "c", "d"]}

    # Creating a dictionary with the nodes and their neighbors.
    G2 = {"a": ["b", "d", "e"], "b": ["a", "c", "e"], "c": ["b", "d", "e"], "d": ["a", "c", "e"],
          "e": ["a", "b", "c", "d"]}

    # Creating a dictionary with the nodes and their neighbors.
    G3 = {"a": ["b", "c", "d"], "b": ["a", "d", "e"], "c": ["a", "b", "d"], "d": ["a", "b", "c", "e"], "e": ["b", "d"]}

    # Creating a dictionary with the nodes and their neighbors.
    Konisberg_bridge = {"a": ["b", "b", "c", "c", "d"], "b": ["a", "a", "d"], "c": ["a", "a", "d"],
                        "d": ["a", "b", "c"]}

    # A graph that has an Euler path.
    test = {"a": ["b", "d"], "b": ["a", "c", "d", "e"], "c": ["b", "f"], "d": ["a", "b", "e", "g"],
            "e": ["b", "d", "f", "h"], "f": ["c", "e", "h", "i"], "g": ["d", "h"], "h": ["e", "f", "g", "i"],
            "i": ["f", "h"]}

    # Creating a list with all the graphs.
    graphs = [G1, G2, G3, Konisberg_bridge, test]
    # Creating a list with the names of the graphs.
    names = ["G1", "G2", "G3", "Konisberg's Bridge", "Test"]

    # Iterating through the list of graphs.
    for i in range(len(graphs)):
        # It prints the name of the graph.
        print(f"Graph {i + 1}: {names[i]}")
        # It prints the graph.
        print(graphs[i])
        # It checks if the graph has an Euler circuit.
        if Euler_circuit(graphs[i]):
            # It prints the message if the graph has an Euler circuit.
            print("The graph has an Euler circuit.")
            # Trying to find an Euler circuit. If it finds one, then it prints it. If it doesn't, then it tries again.
            while True:
                try:
                    # Trying to find an Euler circuit.
                    circuit = finding_Euler_circuit(graphs[i])
                    # It checks if the circuit has all the nodes of the graph.
                    if len(set(circuit)) == len(graphs[i].keys()):
                        # Printing the circuit.
                        print("-".join(circuit))
                        # It breaks the loop.
                        break
                except:
                    # It does nothing. It is used as a placeholder.
                    pass
        else:
            # It prints the message if the graph doesn't have an Euler circuit.
            print("The graph doesn't have an Euler circuit.")
            # It prints the list of odd nodes.
            print(f"List of odd nodes: {odds(graphs[i])}")
        # It prints a blank line.
        print()


# It takes a graph as an input and returns a list of nodes that are odd.
main()

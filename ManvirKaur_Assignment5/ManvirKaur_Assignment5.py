"""
Author: Manvir Kaur
KUID: 3064194
Date: 10/27/2022
Assignment: Assignment05
Purpose: Functions and their properties
Inputs: None except parameters passed on to functions
Outputs: Prints if each relation is a function, bijective, surjective, or injective.
"""


def isFunction(a, b, relation):  # function takes inputs of A, B and a relation to check if the relation is a function
    for i in a:  # for loop created to iterate over each element in A
        n = 0
        for j in b:  # for loop created to iterate over each element in B
            # n will be the number of times a specific element in A and any element in set B are a pair in relation f
            n = n + relation.count((i, j))
        if n != 1:  # if statement to check if an element of A is not assigned to exactly one element of B
            return False  # the relation is not a function
    return True  # True if every element of A is assigned to exactly one element of B making relation is a function


def injective(a, b, relation):  # function takes inputs of A and B and a relation to check if function is injective
    for j in b:  # iterates over the elements of B
        n = 0
        for i in a:  # iterates over the elements of A
            # n will be the number of times any element in A and a specific element in B are a pair in relation f
            n = n + relation.count((i, j))
        if n > 1:  # if statement to check if an element of B is assigned to more than one element of A
            return False  # False if the function is not injective
    return True  # True if the function is injective


def surjective(a, b, relation):  # function takes inputs of A and B and a relation to check if function is surjective
    for j in b:  # iterates over the elements of B
        n = 0
        for i in a:  # iterates over the elements of A
            # n will be the number of times any element in A and a specific element in B are a pair in relation f
            n = n + relation.count((i, j))
        if n < 1:  # if statement to check if an element of B is not assigned to at least one element of A
            return False  # False if the function is not surjective
    return True  # True if the function is surjective


def bijective(a, b, relation):  # function takes inputs of A and B and a relation to check if function is bijective
    if surjective(a, b, relation) and injective(a, b, relation):  # if function is both surjective and injective
        return True  # it is bijective
    else:  # if not both surjective and injective
        return False  # it is not bijective


def inverse(relation):  # function takes in a relation and returns the inverse function
    inverse_function = []  # an empty list created for the inverse function
    for pair in relation:  # for statement to loop through the pairs in the relation
        inverse_function.append((pair[1], pair[0]))  # appends the pairs in reverse to make inverse
    return inverse_function  # inverse function list returned


def printing(num, a, b, relation):  # function to print the given assignment
    print(num)
    print(f"'A = {a}, B = {b}, f = {relation}")  # prints given A, B, and relation
    # prints if the relation is a function
    if isFunction(a, b, relation):
        print('* The relation is a function.')
        if bijective(a, b, relation):  # prints if the relation is bijective
            print('* The relation is bijective.')
            print('* Inverse:', inverse(relation))  # inverse will print only if bijective
        elif injective(a, b, relation):  # prints if the relation is injective
            print('* The relation is injective.')
        elif surjective(a, b, relation):  # prints if the relation is surjective
            print('* The relation is surjective.')
    else:  # prints if relation isn't a function
        print('* The relation is not a function.')
    print("-----------------------------------------------------------------------------------------------------------")


def main():  # main function includes all the inputs given in the assignment instructions
    a1 = ['a', 'b', 'c', 'd']
    b1 = ['v', 'w', 'x', 'y', 'z']
    relation1 = [('a', 'z'), ('b', 'y'), ('c', 'x'), ('d', 'w')]
    printing('\n1.', a1, b1, relation1)

    a2 = ['a', 'b', 'c', 'd']
    b2 = ['x', 'y', 'z']
    relation2 = [('a', 'z'), ('b', 'y'), ('c', 'x'), ('d', 'z')]
    printing('\n2.', a2, b2, relation2)

    a3 = ['a', 'b', 'c', 'd']
    b3 = ['w', 'x', 'y', 'z']
    relation3 = [('a', 'z'), ('b', 'y'), ('c', 'x'), ('d', 'w')]
    printing('\n3.', a3, b3, relation3)

    a4 = ['a', 'b', 'c', 'd']
    b4 = [1, 2, 3, 4, 5]
    relation4 = [('a', 4), ('b', 5), ('c', 1), ('d', 3)]
    printing('\n4.', a4, b4, relation4)

    a5 = ['a', 'b', 'c']
    b5 = [1, 2, 3, 4]
    relation5 = [('a', 3), ('b', 4), ('c', 1)]
    printing('\n5.', a5, b5, relation5)

    a6 = ['a', 'b', 'c', 'd']
    b6 = [1, 2, 3]
    relation6 = [('a', 2), ('b', 1), ('c', 3), ('d', 2)]
    printing('\n6.', a6, b6, relation6)

    a7 = ['a', 'b', 'c', 'd']
    b7 = [1, 2, 3, 4]
    relation7 = [('a', 4), ('b', 1), ('c', 3), ('d', 2)]
    printing('\n7.', a7, b7, relation7)

    a8 = ['a', 'b', 'c', 'd']
    b8 = [1, 2, 3, 4]
    relation8 = [('a', 2), ('b', 1), ('c', 2), ('d', 3)]
    printing('\n8.', a8, b8, relation8)

    a9 = ['a', 'b', 'c']
    b9 = [1, 2, 3, 4]
    relation9 = [('a', 2), ('b', 1), ('a', 4), ('c', 3)]
    printing('\n9.', a9, b9, relation9)


main()

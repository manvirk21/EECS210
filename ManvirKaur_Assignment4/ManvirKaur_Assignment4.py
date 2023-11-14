
"""
Author: Manvir Kaur
KUID: 3064194
Date: 10/13/2022
Assignment: EECS 210 Assignment 4
Last modified: 10/13/2022
Purpose: Code to print properties and closures of sets.
"""


def reflexive(relation, s):  # This function takes a relation and a set, and configures reflexiveness
    print(f"R = {relation}")  # prints the relation R
    for element in s:  # for loop to check each value in the set
        if (element, element) in relation:  # if (e, e) exists in the relation then it is reflexive
            return print("R is reflexive \n")
        else:  # if not reflective
            print(f"R is not reflexive.")
            for value in s:  # for loop to go through each value in s
                relation.add((value, value))  # adds the values to make the relation reflexive
            return print("R* =", relation, "\n")  # prints the closure of R


def symmetric(relation):  # this function takes in a relation and configures symmetry
    print(f"R = {relation}")  # prints the relation R
    for x, y in relation:  # iterates through every pair in the relation
        if (y, x) in relation:  # checks if the (y,x) exists in the relation
            return print("R is symmetric\n")  # prints that R is symmetric
        else:  # if not symmetric
            print("R is not symmetric")  # prints r is not symmetric
            relation.add((y, x))  # adds the proper values to the relation if they don't exist
            return print("R* =", relation, "\n")  # prints the closure of R


def transitive(relation, s):  # this function checks if the relation is transitive by the Warshall matrix
    check = True  # initialize check as True
    for a, b in relation:  # nested for loop to check the transitivity
        for c, d in relation:
            if b == c and (a, d) not in relation:  # if b and c are equal but (a, d) isn't in relation then False
                check = False



def zero_one_matrix(relation, s): # this function returns a matrix where the rows and columns are indexed by
    # the domain and the entries are 1 if the pair is in the set but 0 otherwise
    matrix = [[0 for i in range(len(s))] for j in range(len(s))]  # create an empty nxn matrix
    for i in range(len(s)):
        for j in range(len(s)):
            if (s[i], s[j]) in relation:  # if the pair exists in the relation
                matrix[i][j] = 1  # change the value of the ij entry to be 1
    return matrix  # return the matrix of 0s and 1s


def inv_zero_one_matrix(matrix, domain):  # returns a set of pairs of elements from the domain that are in the matrix
    s = set()
    for i in range(len(domain)):
        for j in range(len(domain)):
            if matrix[i][j] == 1:  # if the ij entry is 1
                # find the corresponding pair from domain and add it to set
                s.add((domain[i], domain[j]))
    return s


def warshall(relation, s):  # takes a binary relation and a domain and returns the transitive closure of the relation
    W = zero_one_matrix(relation, s)
    n = len(W[0])
    for k in range(n):  # iterate n times
        for i in range(n):  # iterate n times
            for j in range(n):  # iterate n times
                # compute a disjunction and a conjunction
                W[i][j] = W[i][j] or (W[i][k] and W[k][j])
    return inv_zero_one_matrix(W, s)


def antisymmetric(s):  # this function determines antisymmetry using pairs in the set
    for (x, y) in s:  # iterates through both x,y
        if (y, x) in s:  # flips them around to y,x
            return False  # since it is antisymmetric if it is symmetric, the function will return False
    return True


def equivalence(relation, s):  # this function checks the equivalence of the relation
    check = True  # initialize check to True
    for a in s:  # for loop initialized for values in the set
        if (a, a) not in relation:  # if statement checks if values are in the relation for reflexiveness
            check = False  # check becomes false
    check2 = True  # second check initialized
    for a, b in relation:  # for loop checks if an ordered pair exists given two variables in the set for symmetry
        if (b, a) not in relation:
            check2 = False
    check3 = True  # third check initialized
    for a in s:  # nested for loop to check transitivity
        for b in s:
            if (a, b) in relation:
                for c in s:
                    if (b, c) in relation and (a, c) not in relation:
                        check3 = False
    if check is True and check2 is True and check3 is True:  # if equivalence is found
        print("b) R is equivalence relation")
        print("c) reflexive is", check, "symmetric is ", check2, "transitive is", check3)
    else:  # if not equivalent
        print("b) R is not equivalence relation")
        print("c) reflexive is ", check, "symmetric is ", check2, "transitive is", check3)


def poset(relation, s):  # determines if a relation of ordered pairs is a poset of the set
    check = True  # initialize check to True
    for a in s:  # for loop initialized for values in the set
        if (a, a) not in relation:  # if statement checks if values are in the relation for reflexiveness
            check = False  # check becomes false
    check2 = True  # second check initialized
    for (x, y) in relation:  # iterates through both x,y
        if (y, x) in relation:  # flips them around to y,x
            check2 = False  # since it is antisymmetric if it is symmetric the function will return False
    check3 = True  # third check initialized
    for a in s:  # nested for loop to check transitivity
        for b in s:
            if (a, b) in relation:
                for c in s:
                    if (b, c) in relation and (a, c) not in relation:
                        check3 = False
    if check is True and check2 is True and check3 is True:  # if the relation is a poset of the set
        print("c) (S,R) is a poset")
        print("d) reflexive is", check, "antisymmetric is ", check2, "transitive is", check3)
    else:  # if not a poset
        print("c) (S,R) is not a poset")
        print("d) Reflexive is", check, ", Antisymmetric is", check2, "transitive is", check3)


def main():
    print("--------------------------------- \nQuestion 1\n---------------------------------\nPart 1")
    R1d = {(1, 1), (4, 4), (2, 2), (3, 3)}
    S1d = {1, 2, 3, 4}
    reflexive(R1d, S1d)

    print("--------------------------------- \nQuestion 1\n---------------------------------\nPart 2")
    R1e = {("a", "a"), ("c", "c")}
    S1e = {"a", "b", "c", "d"}
    reflexive(R1e, S1e)

    print("--------------------------------- \nQuestion 2\n---------------------------------\nPart 1")
    R2d = {(1, 2), (4, 4), (2, 1), (3, 3)}
    symmetric(R2d)

    print("--------------------------------- \nQuestion 2\n---------------------------------\nPart 2")
    R2e = {(1, 2), (3, 3)}
    symmetric(R2e)

    print("--------------------------------- \nQuestion 3\n---------------------------------\nPart 1")
    s3d = {"a", "b", "c", "d"}
    R3d = {("a", "b"), ("d", "d"), ("b", "c"), ("a", "c")}
    print("a) R = ", R3d)
    if transitive(R3d, s3d) == True:
        print("b) R is Transitive")
        print("c) R is Transitive")

    print("--------------------------------- \nQuestion 3\n---------------------------------\nPart 2")
    s3e = {1, 2, 3}
    R3e = {(1, 1), (1, 3), (2, 2), (3, 1), (3, 2)}
    print("a) R = ", R3e)
    if transitive(R3e, s3e) == False:
        print("b) R is not transitive")

    print("--------------------------------- \nQuestion 4\n---------------------------------\nPart 1")
    s4d = {1, 2, 3}
    r4d = {(1, 1), (2, 2), (2, 3)}
    print("a) R is ", r4d)
    equivalence(r4d, s4d)

    print("--------------------------------- \nQuestion 4\n---------------------------------\nPart 2")
    s4e = {"a", "b", "c"}
    r4e = {("a", "a"), ("b", "b"), ("c", "c"), ("b", "c"), ("c", "b")}
    print("a) R is", r4e)
    equivalence(r4e, s4e)

    print("--------------------------------- \nQuestion 5\n---------------------------------\nPart 1")
    s5d = {1, 2, 3, 4}
    r5d = {(1, 1), (1, 2), (2, 2), (3, 3), (4, 1), (4, 2), (4, 4)}
    print("a) S =", s5d)
    print("b) R =", r5d)
    poset(r5d, s5d)

    print("--------------------------------- \nQuestion 5\n---------------------------------\nPart 2")
    s5e = {0, 1, 2, 3}
    r5e = {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)}
    print("a) S =", s5e)
    print("b) R =", r5e)
    poset(r5e, s5e)

main()
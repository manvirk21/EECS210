"""
Author: Manvir Kaur
KUID: 3064194
Date: 09/29/2022
Assignment: Assignment03
Last modified: 09/29/2022
Purpose: Demonstrating operations on relations and properties of relations.
"""


# Problem number 1
def problem_1(r1, r2):
    print(f"1a) union of R1 and R2 {r1.union(r2)}")  # calls union function to print union between R1 and R2
    print(f"1b) intersection of R1 and R2 {r1.intersection(r2)}")  # calls intersection function and prints the result
    print(f"1c) difference of R1 and R2 {r1.difference(r2)}")  # calls difference between R1 and R2 and prints result
    print(f"1d) difference of R2 and R1 {r2.difference(r1)}")  # calls difference between R2 and R1 and print the result


R1 = {(1, 1), (2, 2), (3, 3)}  # initializes set R1
R2 = {(1, 1), (1, 2), (1, 3), (1, 4)}  # initializes set R2
problem_1(R1, R2)  # calls problem_1 function with R1 and R2 as the parameters to conduct the functions.


# Functions for problem number 2 and 3
def relation(x, y):  # the function returns True if x + y is equal to 0, otherwise returns False.
    return x + y == 0  # x will be the first number to be compared and y is the y-coordinate of the point


def composition(r, s):  # r and s are different sets of ordered pairs
    """
    takes two sets of tuples and returns a new set where each tuple is the concatenation of tuple from the first set and
    one from the second set if the second element of the first set matches the first element of the second set
    """
    # returns a set of every pair (i,j) if i is in r and j is in s and i is related to j in r.
    return {(i[0], j[1]) for i in r for j in s if i[1] == j[0]}


# Functions to solve problem number 4
def reflexive(s, domain):  # function takes in two parameters: a set of ordered pairs and a domain
    # The function returns True if the relation is reflexive and False otherwise
    return not (False in [(x, x) in s for x in domain])  # no pair in domain where relation is false means reflexive


def symmetric(s):  # function that takes in a set of ordered pairs to check symmetry
    return {(y, x) for (x, y) in s} == s  # returns True if the set s is symmetric, and False otherwise following rule


def antisymmetric(s):  # function that takes in a set of ordered pairs to check antisymmetry
    if symmetric(s):  # if s was symmetric then it can't be antisymmetric
        return False
    for (x, y) in s:
        if (y, x) in s:
            return False  # if (x,y) exists then (y,x) can't exist in s in order to be antisymmetric as per the rule
    return True  # returns True if antisymmetric as per the rules checked above


def transitive(s):  # function that takes in a set of ordered pairs to check transitivity
    for w, x in s:  # the pair (w, x) exists in s
        for y, z in s:  # the pair (y, z) also exists in s
            if x == y and (w, z) not in s:  # if x is equal to y then the pair (w, z) must also exist in the set s
                return False  # if it doesn't exist in s then the set is not transitive
    return True  # returns true if the set is transitive


R = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}  # defining the set R
S = {(1, 0), (2, 0), (3, 1), (3, 2), (4, 1)}  # defining the set S
print(f"\n2) S composition R\n —> {composition(S, R)}")  # finding the composition between S and R
print(f"\n3) R composition R\n —> {composition(R, R)}")  # finding the composition between R and R

domain = [i for i in range(-10, 11)]  # defining the domain for number 4
pairs = {(x, y) for x in domain for y in domain if relation(x, y)}  # creating pairs from domain to satisfy the relation
print(f"\n4a) Ordered pairs: \n —> {pairs}")  # printing the ordered pairs
print(f"4b) Reflexive?: \n —> {reflexive(pairs, domain)}")  # checking if the pairs are reflexive
print(f"4c) Symmetric?: \n —> {symmetric(pairs)}")  # checking if the pairs are symmetric
print(f"4d) Antisymmetric?: \n —> {antisymmetric(pairs)}")  # checking if the pairs are antisymmetric
print(f"4e) Transitive?: \n —> {transitive(pairs)}")  # checking if the pairs are transitive

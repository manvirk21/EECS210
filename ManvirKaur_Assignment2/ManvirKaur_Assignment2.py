"""
Author: Manvir Kaur
KUID: 3064194
Date: 09/15/2022
Assignment: Assignment01
Last modified: 09/15/2022
Purpose: Printing truth values of predicates and propositions
"""

domain = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # defining the domain of the values of x


# The start of problem number 1
def problem1():
    # 1a) ∃x P(x), where P(x) is the statement “x<2”
    print("------------------------------------------------------------------------------------------")  # line breaker
    print("1a) ∃x P(x), where P(x) is the statement “x<2”")  # print the problem
    validation = False  # validation initialization to False
    for x in domain:  # creating a for loop that will iterate through every element in domain
        if x < 2:  # if statement to check if x is less than 2
            validation = True  # changing the validation to True because statement has been proven
            print(f"--> {x} < 2, hence proving the statement True")  # prints what value makes statement true
            break  # break the loop when the condition is true to avoid multiple iterations
    if not validation:  # if statement in case validation is still false
        print("False, no values in the domain prove the statement to be True")  # prints False

    print("------------------------------------------------------------------------------------------")  # line breaker
    print("1b) ∀x P(x), where P(x) is the statement “x<2”")  # prints the problem
    validation = True  # validation initialization to True
    for x in domain:  # creating a for loop that will iterate through every element in domain
        if not (x < 2):  # if statement to check if x is not less than 2
            validation = False  # changing the validation to False because statement has been proven not True
            print(f"--> {x} >= 2, hence proving the statement False")  # prints value where P(x) is False
            break  # break the loop when the condition is False to avoid multiple iterations
    if validation:  # if statement in case validation is still True
        print("All values in the domain satisfy the statement")  # prints the satisfaction

    print("------------------------------------------------------------------------------------------")  # line breaker
    print("1c) ∃x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is the statement “x>7”")  # problem
    validation = False  # validation initialization to False
    for x in domain:  # creating a for loop that will iterate through every element in the domain
        if (x < 2) or (x > 7):  # if statement to check if x is not less than 2 or more than 7
            validation = True  # changing the validation to False because statement has been proven not True
            print(f"--> {x} < 2 or {x} > 5, hence proving the statement True")  # prints value where P(x) is True
            break  # break the loop when the condition is True to avoid multiple iterations
    if not validation:  # if statement in case validation is still False
        print("False, no values in the domain prove the statement to be True")  # prints False

    print("------------------------------------------------------------------------------------------")  # line breaker
    print("1d) ∀x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is the statement “x>7”")  # question
    validation = True  # validation initialization to True
    for x in domain:  # creating a for loop that will iterate through every element in domain
        if not (x < 2 or x > 7):  # if statement to check if x is not less than 2 or greater than 7
            validation = False  # changing the validation to False because statement has been proven not True
            print(f"--> 2 < (x = {x}) < 7, hence proving the statement False")  # prints value where P(x) is False
            break  # break the loop when the condition is False to avoid multiple iterations
    if validation:  # if statement in case validation is still True
        print("All values in the domain satisfy the statement")  # prints the satisfaction

    print("------------------------------------------------------------------------------------------")  # line breaker
    print("1e) Prove De Morgan’s Law for the Existential Quantifier where P(x) is the statement “x<5”")  # statement
    print("prove !∃x (x < 5) == ∀x (x >= 5) \nFirst proving: not(for some P(x), the negation")
    validation_E = True  # validation initialization to True
    for x in domain:  # creating a for loop that will iterate through every element in domain
        if x < 5:  # if statement to check if x is less than 5
            validation_E = False  # changing the validation to False because statement has been proven not True
            validation = not validation_E
            print(f"--> {x} < 5 proves the statement is {validation_E} and the negation of that is {validation}")
            break  # break the loop when the condition is False to avoid multiple iterations
        if validation_E:
            print("All values in the domain satisfy the statement")  # prints the satisfaction
    print("------------------------------------------------------------------------------------------")  # line breaker
    print("Proving: for all (not(P(x))")
    validation_A = False  # validation initialization to True
    for x in domain:  # creating a for loop that will iterate through every element in domain
        if x >= 5:  # if statement to check if x is greater than or equal to 5
            validation_A = True  # changing the validation to False because statement has been proven not True
            print(f"--> not({x} >= 5), proving {validation_A}")  # prints value where P(x) is False
            print("Since the negation and ∀x (x >= 5) proven True the statement is True")
            break  # break the loop when the condition is True to avoid multiple iterations
        if validation_A:
            print("No values in the domain satisfy the statement")  # prints the satisfaction

    print("------------------------------------------------------------------------------------------")  # line breaker
    print("1f) Prove De Morgan’s Law for the Universal Quantifier where P(x) is the statement “x<5”")  # statement
    print("prove !∀x (x < 5) == ∃x (x >= 5)\nFirst proving: not(for all P(x), the negation")
    validation_A = True  # validation initialization to True
    for x in domain:  # creating a for loop that will iterate through every element in domain
        if x < 5:  # if statement to check if x is less than 5
            validation_A = False  # changing the validation to False because statement has been proven not True
            validation = not validation_A
            print(f"--> {x} < 5 proves the statement is {validation_A} and the negation of that is {validation}")
            break  # break the loop when the condition is False to avoid multiple iterations
        if validation_E:
            print("All values in the domain satisfy the statement")  # prints the satisfaction
    print("------------------------------------------------------------------------------------------")  # line breaker
    print("Proving: for some (not(P(x))")
    validation_A = False  # validation initialization to True
    for x in domain:  # creating a for loop that will iterate through every element in domain
        if x >= 5:  # if statement to check if x is greater than or equal to 5
            validation_A = True  # changing the validation to False because statement has been proven not True
            print(f"--> not({x} >= 5), proving {validation_A}")  # prints value where P(x) is False
            print("Since the negation and ∃x (x >= 5) are proven True the overall statement is True")
            break  # break the loop when the condition is True to avoid multiple iterations
        if validation_A:
            print("No values in the domain satisfy the statement")  # prints the satisfaction


def problem2():
    def p(x, y):  # creates a function for P(x,y): x ∙ y = 0
        return x*y == 0
    print("\n------------------------------------------------------------------------------------------")  # breaker
    print("2a) ∀x∀yP(x,y)")  # prints the problem statement
    validation = True  # validation initialization to True
    for x in domain:  # for statement iterates through every element in domain
        for y in domain:  # for statement iterates through every element in domain
            if not p(x, y):  # if the condition is not satisfied
                validation = False  # changing the validation to False since condition not satisfied
                print(f"--> {validation} For (x, y) = {(x, y)}, xy = {x * y} proves the statement wrong")  # False case
                break  # breaks the loop when the condition is False to avoid multiple iterations
            if not validation:
                break  # break out of loop
    if validation:  # if validation is True then all the values will satisfy the statement
        print("True, all values in the domain prove the statement")

    print("------------------------------------------------------------------------------------------")  # line breaker
    print("2b) ∀x∃yP(x,y)")  # prints the problem statement
    values = []  # creates an empty list named values to store the satisfying cases
    for x in domain:  # for loop iterates through every element in the domain
        validation = False  # validation initialization to False
        for y in domain:  # iterates through every element in the domain
            if p(x, y):  # if statement checks that condition is satisfied
                validation = True  # changes validation to True
                values.append((x, y))  # appends the value to the list because it satisfies the statement
                break  # break out to avoid repetition
        if validation is False:  # if validation is still False after the iteration
            break  # break out
    if validation:  # if True meaning condition is satisfied
        print("True")
        for value in values:  # print all the values
            print(f"--> (x, y) = {value} satisfies the problem statement xy = 0")
    else:
        print("False, no values of xy satisfy the problem statement")  # else print no cases satisfy the statement

    print("------------------------------------------------------------------------------------------")  # line breaker
    print("2c) ∃x∀yP(x,y)")  # prints the problem statement
    for x in domain:  # for loop iterates through every element in domain
        validation = True  # validation initialization to true
        for y in domain:  # for loop iterates through every element in domain
            if not p(x, y):  # if the condition is not satisfied
                validation = False  # validation is set to False as condition is not satisfied
                break  # break out because condition isn't satisfied
        if validation is True:  # if statement checks if validation is still true and all y values satisfy the condition
            print(f"--> {validation}, for x = {x}, the proposition is true for all values of y")  # valid x value print
            break  # break out after print is completed
    if not validation:  # if no values satisfy the problem statement then:
        print("False")  # print False because validation is False
        print("No values of (x, y) satisfy the proposition")  # no values  satisfy the problem statement

    print("------------------------------------------------------------------------------------------")  # line breaker
    print("2d) ∃x∃yP(x,y)")  # prints the problem statement
    for x in domain:  # for loop iterates through every element in domain
        validation = False  # validation initialization to false
        for y in domain:  # for loop iterates through every element in domain
            if p(x, y):  # if the problem statement is satisfied:
                validation = True  # the validation is set to True as the problem is satisfied
                print(f"--> {validation}: for (x, y) = {(x, y)}, xy = {x * y} proves the statement true")  # valid pair
                break  # break out of loop as valid pair is found
        if validation:
            break  # if condition satisfies then quit
    if not validation:
        print("no value of x, y satisfy the problem statement")  # prints if no valid cases are found


problem1()  # initiates problem 1
problem2()  # initiates problem 2

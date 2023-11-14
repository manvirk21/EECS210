"""
Author: Manvir Kaur
KUID: 3064194
Date: 08/29/2022
Assignment: Assignment01
Last modified: 09/01/2022
Purpose: Printing Truth Tables
"""


# returns the truth table to prove De Morgan's First Law
def DMFL(p, q):  # Function defined to prove De Morgan's First Law with the parameters p and q.
    top_header = ["p", "q", "!p", "!q", "p*q", "!(p*q)", "!p+!q"]  # New list is created with a string of the equations.
    values = [p, q, not p, not q, p and q, not (p and q), not p or not q]  # List that actually computes Bool values.
    return top_header, values  # The function ends by returning the string and Boolean values


# returns the truth table to prove De Morgan's Second Law
def DMSL(p, q):  # Function defined to prove De Morgan's Second Law with the parameters p and q.
    top_header = ["p", "q", "!p", "!q", "p*q", "!(p+q)", "!p*!q"]  # New list is created with a string of the equations.
    values = [p, q, not p, not q, p and q, not (p or q), not p and not q]  # List that actually computes Bool values.
    return top_header, values  # The function ends by returning the string and Boolean values


# returns the truth table to prove the First Associate Law
def first_associate(p, q, r):  # Function defined to prove The First Associate Law with the parameters p and q.
    top_header = ["p", "q", "r", "p*q", "q*r", "(p*q)*r", "p*(q*r)"]  # New list is created with a string of the
    # equations.
    values = [p, q, r, p and q, q and r, (p and q) and r, p and (q and r)]  # List that actually computes Bool values.
    return top_header, values  # The function ends by returning the string and Boolean values


# return the truth table to prove the Second Associate Law
def second_associate(p, q, r):  # Function defined to prove The Second Associate Law with the parameters p and q.
    top_header = ["p", "q", "r", "p+q", "q+r", "(p+q)+r", "p+(q+r)"]  # New list is created with a string of the
    # equations.
    values = [p, q, r, p or q, q or r, (p or q) or r, p or (q or r)]  # List that actually computes Boolean values.
    return top_header, values  # The function ends by returning the string and Boolean values


# return the truth table to prove (p ∨ q) ∧ (p → r) ∧ (q → r)] → r ≡ T
def first_equation(p, q, r):  # Function defined to prove the above equation
    top_header = ["p", "q", "r", "!p", "!q", "!r", "p+q", "!p+r", "!q+r", "[(p+q)*(p->r)*(q->r)]->r", "True"]  # New
    # list is created with a string of the equations.
    values = [p, q, r, not p, not q, not r, p or q, not p or r, not q or r, not ((p or q) and (not p or r) and
                                                                                 (not q or r)) or r, True]  # List
    # that actually computes Boolean values is created.
    return top_header, values  # The function ends by returning the string and Boolean values


# returns the truth table to prove p ↔ q ≡ (p → q) ∧ (q → p)
def second_equation(p, q):  # Function defined to prove the above equation.
    top_header = ["p", "q", "!p", "!q", "p+q", "!p+q", "!q+p", "p*q", "!p*!q", "(p<->q)", "(p->q)*(q->p)"]  # New
    # list is created with a string of the equations.
    values = [p, q, not p, not q, p or q, not p or q, not q or p, p and q, not p and not q, (not p or q) and
              (not q or p), (p and q) or (not p and not q)]  # List that actually computes Boolean values is created.
    return top_header, values  # The function ends by returning the string and Boolean values


# main function is created to run all the other functions and print the truth tables
def main():  # the main function is defined
    p = [True, False]  # p, q, and r are assigned the Boolean values in the form of a list.
    q = [True, False]
    r = [True, False]
    pq_truth_table = [DMFL, DMSL, second_equation]  # List of truth tables with only two variables
    truth_tables = [DMFL, DMSL, first_associate, second_associate, first_equation, second_equation]  # List of the
    # truth tables that have three variables.
    print("==" * 50)  # prints a border on the top because it looks better if it's included there
    for table_generate in truth_tables:  # for loop is created to loop through the list of truth tables.
        if table_generate in pq_truth_table:  # if statement determines the number of variables to determine next step
            for i in p:  # Next there is a nested for loop. This goes through the Boolean values in p.
                for j in q:  # This helps loop through the Boolean values in q.
                    top_header, values = table_generate(i, j)  # the top_header and values are assigned within the
                    # table generator as parameters
                    if i is True and j is True:  # this if statement checks to see that the row of the truth table the
                        # for loop is looking at is the header
                        print(*top_header, sep='\t\t|')  # printing the equations as the header separated by 2 tabs.
                    print(*values, sep='\t|')  # prints the truth table values by row separated by one tab.
            print("==" * 50)  # the "==" string multiplied by 50 prints after each truth table as a divisor.
        else:  # the code below is for the equations with more than two variables.
            for i in p:  # this time there is a triple nested for loop. Loops through the values in the list p.
                for j in q:  # loops through the values in the list q.
                    for k in r:  # loops through the values in the list r.
                        top_header, values = table_generate(i, j, k)  # top_header and values are assigned to the
                        # table generator.
                        if i is True and j is True and k is True:  # this if statement checks to see that the row of
                            # the truth table the for loop is looking at is the header
                            print(*top_header, sep='\t\t|')  # printing the equations as the header separated by 2 tabs.
                        print(*values, sep='\t|')  # prints the truth table by row
            print("==" * 50)  # the "==" string multiplied by 50 prints after each truth table as a divisor.


main()  # the main function is called so that everything can run properly.

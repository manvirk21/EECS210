"""
Author: Manvir Kaur
KUID: 3064194
Date: 11/29/22
Assignment: 07
Purpose:
"""

# Importing the math module.
import math
# Importing the comb function from the math module.
from math import comb


def first(objects, items, boxes):
    """
    There are (objects!) / ((items!)^boxes * (objects - (boxes * items))!) ways to distribute objects into boxes,
    where each box contains items.
    
    :param objects: The total number of objects
    :param items: The number of items in each box
    :param boxes: The number of boxes you have
    """
    # This is calculating the number of ways to distribute objects into boxes, where each box contains items.
    total = math.factorial(objects) // (((math.factorial(items)) ** boxes) * (math.factorial(objects - (boxes * items))))
    # This is printing the total number of ways.
    print("There are " + str(total) + " ways")


def second(in_object, boxes):
    """
    The function takes in an integer and a list of integers, and returns the number of ways to choose
    the integers in the list from the integer
    
    :param in_object: The number of objects you have to choose from
    :param boxes: the number of boxes
    :return: The number of ways to choose boxes from in_object.
    """
    # Assigning the factorial function to the variable f.
    f = math.factorial
    # Calculating and returning the number of ways to choose boxes from in_object.
    return (f(in_object) // f(boxes)) // f(in_object - boxes)


def third(objects, in_boxes):
    """
    For each box, we add the number of ways to put the objects in that box, and then we add the number
    of ways to put the objects in that box and the next box, and then we add the number of ways to put
    the objects in that box, the next box, and the next box, and so on
    
    :param objects: The number of objects you have
    :param in_boxes: The number of boxes you have
    """
    # Initializing the variable total to 0.
    total = 0
    # Iterating through the number of boxes.
    for i in range(1, in_boxes + 1):
        # Initializing the variable subtotal to 0.
        subtotal = 0
        # Iterating through the number of boxes.
        for j in range(0, i):
            # Calculating the number of ways to put the objects in that box, and then we add the number of ways to
            # put the objects in that box and the next box and so on.
            subtotal += ((-1) ** j) * (comb(i, j)) * ((i - j) ** objects)
        # Calculating the number of ways to put the objects in that box, and then we add the number of ways to put
        # the objects in that box and the next box and so on.
        total += ((1 / math.factorial(i)) * subtotal)
    # Printing the total number of ways.
    print(f'There are {total} number of ways.')


def fourth(in_objects, in_boxes):
    """
    This function gives the number of ways of indistinguishable objects as a sum of exactly indistinguishable box terms
    or the number of partitions into parts of which the largest is exactly in_boxes.

    The first base case is when in_objects is less than in_boxes. There are no ways of putting in_objects
    indistinguishable objects into in_boxes boxes. The second base case is when in_objects is equal to in_boxes.
    There is only one way of putting indistinguishable objects into indistinguishable boxes. The third base case is
    when in_boxes is zero. In this case, there are no ways of putting the indistinguishable objects into the
    indistinguishable boxes.
    
    :param in_objects: the number of objects
    :param in_boxes: the number of boxes
    :return: The number of ways of indistinguishable objects as a sum of exactly indistinguishable box
    terms or the number of partitions into parts of which the largest is exactly in_boxes.
    """
    # This is a base case for the function. If the number of objects is less than the number of boxes, then there are
    # no ways of putting the objects into the boxes.
    if in_objects < in_boxes:
        return 0
    # This is a base case for the function. If the number of objects is equal to the number of boxes, then there is
    # only one way of putting the objects into the boxes.
    if in_objects == in_boxes:
        return 1
    # This is a base case for the function. If the number of boxes is zero, then there are no ways of putting the
    # objects into the boxes.
    if in_boxes == 0:
        return 0
    # This is a recursive function. It is calling the function fourth with the arguments in_objects - 1 and in_boxes
    # - 1, and then it is adding the result of that function call to the result of the function call fourth with the
    # arguments in_objects - in_boxes and in_boxes.
    return fourth(in_objects - 1, in_boxes - 1) + fourth(in_objects - in_boxes, in_boxes)


def main():  # the main function is primarily responsible for printing each problem using the above functions
    # printing problem 1a
    print("1a: ")
    objects = 52
    boxes = 4
    item = 5
    first(objects, item, boxes)
    print("——————————————————————————————————————————————————————————————————————————————")  # printing a divider
    # printing problem 1b
    print("1b: ")
    objects = 40
    boxes = 4
    item = 10
    first(objects, item, boxes)

    print("——————————————————————————————————————————————————————————————————————————————")
    print("\n2a: ")  # printing problem 2a
    n = 10
    r = 8
    # calling function to find the combinations
    print("{} ways".format((second(n + r - 1, n))))
    print("——————————————————————————————————————————————————————————————————————————————")
    print("2b: ")  # printing problem 2b
    n = 12
    r = 6
    # calling function to find the combinations
    print("{} ways".format((second(n + r - 1, n))))

    print("——————————————————————————————————————————————————————————————————————————————")
    print("\n3a: ")  # printing problem 3a
    dist_object = 4
    in_box = 3
    third(dist_object, in_box)
    print("——————————————————————————————————————————————————————————————————————————————")
    print("3b: ")  # printing problem 3b
    dist_object = 5
    in_box = 4
    third(dist_object, in_box)

    print("——————————————————————————————————————————————————————————————————————————————")
    print("\n4a: ")  # printing problem 4a
    in_objects = 6
    in_boxes = 4
    count = 0
    # This is iterating through the number of boxes.
    for i in range(in_boxes):
        # Calling the function fourth with the arguments in_objects and i + 1, and then it is
        # assigning the result of that function call to the variable new_count.
        new_count = fourth(in_objects, i + 1)
        # Adding the result of the function call fourth with the arguments in_objects and i + 1 to the variable count.
        count = count + new_count
    # This is printing the total number of ways of writing n as a sum of in_boxes terms.
    print("Total number of ways of writing n as a sum of", in_boxes, "terms is ", count)

    print("——————————————————————————————————————————————————————————————————————————————")
    print("\n4b: ")  # printing problem 4b
    in_objects = 5
    in_boxes = 3
    # The variable count is being initialized to 0.
    count = 0
    # Iterating through the number of boxes.
    for i in range(in_boxes):
        # Calling the function fourth with the arguments in_objects and i + 1, and then it is
        # assigning the result of that function call to the variable new_count.
        new_count = fourth(in_objects, i + 1)
        # Adding the result of the function call fourth with the arguments in_objects and i + 1 to the variable count.
        count = count + new_count
    # This is printing the total number of ways of writing n as a sum of in_boxes terms.
    print("Total number of ways of writing n as a sum of", in_boxes, "terms is ", count)


main()

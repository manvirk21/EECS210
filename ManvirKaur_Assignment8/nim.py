# Nim is a game where players take turns removing objects from heaps.
class Nim:
    def __init__(self, num, stage):
        """
        The function __init__() is a constructor that initializes the class variables
        
        :param num: the number of the node
        :param stage: This is the current stage of the game
        """
        # Initializing the class variable num.
        self._num = num
        # Initializing the class variable stage.
        self._stage = stage
        # Initializing the class variable children.
        self._children = []
        # Initializing the class variable min_max.
        self._min_max = None
        # Calling the function possible()
        self.possible()

    def adding_child(self, child):
        """
        This function adds a child to the list of children.
        
        :param child: The child node to be added to the current node
        """
        # This is adding the child node to the list of children.
        self._children.append(child)

    def children_num(self):
        """
        It returns the number of children of the node.
        :return: The number of children
        """
        # It returns the number of children of the node.
        return self._children

    def set_min_max(self, num):
        """
        The function set_min_max() takes in a number and sets the instance variable _min_max to that
        number
        
        :param num: The number of the min/max to set
        """
        # Setting the instance variable _min_max to the number that is passed in.
        self._min_max = num

    def __str__(self):
        """
        The function returns a string that contains the stage of the node, the number of the node, and
        the min/max value of the node
        :return: The min and max values of the array.
        """
        # This is returning the stage of the node, the number of the node, and the min/max value of the node.
        return "\t" * self._stage + f"{self._num}: min/max = {self._min_max}"

    def __lt__(self, other):
        """
        If the other object is an integer, then compare the min_max attribute of the current object to
        the other object. If the other object is not an integer, then compare the min_max attribute of
        the current object to the min_max attribute of the other object
        
        :param other: The other object to compare to
        :return: The minimum value of the range.
        """
        # Checking if the other object is an integer.
        if isinstance(other, int):
            # Comparing the min_max attribute of the current object to the other object.
            return self._min_max < other
        else:
            # Comparing the min_max attribute of the current object to the min_max attribute of the other object.
            return self._min_max < other._min_max

    def printing(self):
        """
        It prints the current node, then calls the printing function on each of its children
        """
        # Printing the current node.
        print(self)
        # Iterating through the list of children and calling the printing function on each of them.
        for child in self._children:
            # Calling the printing function on each of the children.
            child.printing()

    def possible(self):
        """
        For each number in the list, we subtract every possible number from it, and if the resulting
        list is not in the list of possible lists, we add it to the list of possible lists, and create a
        new node with the resulting list as its number list
        """
        # Creating an empty list.
        p_list = []
        # This is iterating through the list of numbers.
        for n in range(len(self._num)):
            # This is iterating through the list of numbers.
            for num in range(1, self._num[n] + 1):
                # Creating a copy of the list.
                value = self._num[:]
                # Subtracting the number from the value.
                value[n] -= num

                # Checking if the sorted value is not in the list of possible lists and the value is not equal to 0.
                if sorted(value) not in p_list and value is not [0]*(len(self._num)):
                    # Adding the sorted value to the list of possible lists.
                    p_list.append(sorted(value))
                    # Creating a new node with the resulting list as its number list.
                    node = Nim(value, self._stage + 1)
                    # Adding the child node to the list of children.
                    self.adding_child(node)
        # This is checking if the list of possible lists is empty.
        if len(p_list) == 0:
            # This is checking if the stage is even.
            if self._stage % 2 == 0:
                # This is setting the min/max value of the node to -1.
                self._min_max = -1
            else:
                # This is setting the min/max value of the node to 1.
                self._min_max = 1
        else:
            # This is checking if the stage is even.
            if self._stage % 2 == 0:
                # This is setting the min/max value of the node to the maximum value of the children.
                self._min_max = max(self._children)._min_max
            else:
                # This is setting the min/max value of the node to the minimum value of the children.
                self._min_max = min(self._children)._min_max


# Creating a new node with the list [2, 2, 1] as its number list and 0 as its stage.
test1 = Nim([2, 2, 1], 0)
# Printing the current node, then calls the printing function on each of its children.
test1.printing()
# This is printing the statement "Player 1 has higher chances to win" if the min/max value of the node
# is 1, otherwise it prints the statement "Player 2 has higher chances to win".
print("\nPlayer 1 has higher chances to win" if test1._min_max == 1 else "\nPlayer 2 has higher chances to win")

# Printing a line of dashes to separate the two test cases.
print("---------------------------------------------------------------------")
# Creating a new node with the list [1, 2, 3] as its number list and 0 as its stage.
test2 = Nim([1, 2, 3], 0)
# It prints the current node, then calls the printing function on each of its children.
test2.printing()
# This is printing the statement "Player 1 has higher chances to win" if the min/max value of the node
# is 1, otherwise it prints the statement "Player 2 has higher chances to win".
print("\nPlayer 1 has higher chances to win" if test2._min_max == 1 else "\nPlayer 2 has higher chances to win")
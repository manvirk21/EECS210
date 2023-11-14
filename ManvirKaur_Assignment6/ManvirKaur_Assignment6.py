"""
Author: Manvir Kaur
KUID: 3064194
Date: 11/10/2022
Assignment: Assignment06
Purpose: Solving Sudoku board
"""


def is_good(i, j, x, grid):
    """
    "If the number is not in the row, column, or box, then it's good."
    
    Now, we can write a function to solve the sudoku
    
    :param i: the row of the cell we're trying to fill
    :param j: the column we're currently on
    :param x: the number we're trying to place
    :param grid: the sudoku grid
    :return: A boolean value.
    """
    # This is checking if the number is in the row.
    for col in range(9):
        if grid[i][col] == x:
            return False
    # This is checking if the number is in the column.
    for row in range(9):
        if grid[row][j] == x:
            return False
    # This is finding the starting row of the box that the cell is in.
    start_row = i - i % 3
    # This is finding the starting column of the box that the cell is in.
    start_col = j - j % 3

    # This is checking if the number is in the box.
    r = start_row
    while r <= start_row + 2:
        # This is finding the starting column of the box that the cell is in.
        c = start_col
        # checking if the number is in the box.
        while c <= start_col + 2:
            # This is checking if the number is in the box.
            if grid[r][c] == x:
                # Returning the value False.
                return False
            # This is incrementing the value of c by 1.
            c += 1
        # This is incrementing the value of r by 1.
        r += 1
    # Returning the value True.
    return True


def solve_helper(i, j, grid):
    """
    If the current cell is empty, try all possible numbers and recurse
    
    :param i: the row of the grid
    :param j: the column
    :param grid: a 9x9 list of lists, where each list represents a row in the grid
    :return: A boolean value.
    """
    # This is checking if the current cell is empty, if it is not empty, then it prints the grid.
    if i == 8 and j == 8:
        # This is checking if the current cell is empty, if it is not empty, then it prints the grid.
        if grid[i][j] != 0:
            # Iterating through the grid.
            for row in grid:
                # Iterating through the row.
                for n in row:
                    # Printing the numbers in the grid with a space between them.
                    print(n, end=" ")
                # Printing a blank line.
                print()
        else:
            for x in range(1, 10):
                # This is checking if the number is in the row, column, or box.
                if is_good(i, j, x, grid) is True:
                    # Assigning the value of x to the grid at the position of i and j.
                    grid[i][j] = x
                    for row in grid:  # Iterating through the grid.
                        for n in row:  # Iterating through the row.
                            # Printing the numbers in the grid with a space between them.
                            print(n, end=" ")
                        # Printing a blank line.
                        print()
                    # Assigning the value of 0 to the grid at the position of i and j.
                    grid[i][j] = 0
        print()
        return
    # This is checking if the column is greater than 8, if it is, then it will call the function again with the next
    # row and the first column.
    elif j > 8:
        # This is calling the function again with the next row and the first column.
        solve_helper(i + 1, 0, grid)

    # This is checking if the current cell is empty, if it is not empty, then it prints the grid.
    elif grid[i][j] == 0:
        # Checking if the number is in the row.
        for x in range(1, 10):
            # This is checking if the number is in the row, column, or box.
            if is_good(i, j, x, grid) is True:
                # Assigning the value of x to the grid at the position of i and j.
                grid[i][j] = x
                # This is calling the function again with the next column.
                solve_helper(i, j + 1, grid)
                # Assigning the value of 0 to the grid at the position of i and j.
                grid[i][j] = 0
        return
    # This is checking if the column is greater than 8, if it is, then it will call the function again with the next
    # row and the first column.
    else:
        # This is calling the function again with the next column.
        return solve_helper(i, j + 1, grid)


def solveSudoku(grid):
    """
    We start at the top left corner of the grid, and recursively try to fill in the grid with numbers
    from 1 to 9. 
    
    If we can't fill in a number, we backtrack and try a different number. 
    
    If we reach the end of the grid, we return True. 
    
    If we reach a point where we can't fill in a number, we return False.
    
    :param grid: the sudoku grid
    """
    # Calling the function solve_helper with the parameters 0, 0, and grid.
    solve_helper(0, 0, grid)


def main():
    """
    The function takes in a file name, opens the file, reads the file, and then passes the puzzle to the
    solveSudoku function.
    """
    files = ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt", "puzzle4.txt", "puzzle5.txt"]  # list of all the files
    for file in files:  # iterate through all files
        with open(file=file, mode="r") as f:  # open files
            puzzle = []  # Creating an empty list.
            for line in f:  # read each line
                # This is creating a list of lists, where each list represents a row in the grid.
                puzzle.append([int(i) if i.isnumeric() else 0 for i in line.split()])
        print(f"Filename: {file}")  # print file name
        print("Before: ")
        print(puzzle)  # printing the puzzle
        print("---------------------------------------")  # divider
        print("Solved: ")
        # Calling the function solveSudoku and passing the puzzle as a parameter.
        solveSudoku(puzzle)


main()

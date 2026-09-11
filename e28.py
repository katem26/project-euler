# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
"""
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
"""
# The sum on the diagonals is 101
# what is the sum on the diagonals of a 1001 by 1001 spiral?

""" each smaller square in the center e.g.
7 8 9
6 1 2
5 4 3
has four corners (3, 5, 7, and 9 in this case)
the difference between each corner increases by two each time
(3x3 square has 3,5,7,9 (difference of two), 4x4 square has 13,17,21,25 (difference of four))"""

def calculate_diagonal_sum(gridSize):
    total = 1
    last_number_added = 1

    for corner_difference in range(2,gridSize,2):
        for corner in range(0,4):
            current_number = last_number_added + corner_difference
            total += current_number
            last_number_added = current_number

    return total

print(calculate_diagonal_sum(1001))



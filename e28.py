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

def calcDiag(gridSize):
    answer = 1
    prev = 1
    for j in range(2,gridSize,2):
        for i in range(0,4): # for each corner (1st loop is 3,5,7,9, second loop is 13,17,21,25...)
            num = prev+j
            answer+=num
            prev=num

    return answer

print(calcDiag(1001))



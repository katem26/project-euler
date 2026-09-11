# find the smallest positive integer such that x, 2x, 3x, 4x, 5x, and 6x contain the same digits

def same_digits(x, y):
    if len(str(x)) != len(str(y)): # if the strings are different lengths, they cannot be permutations of each other
        return False

    digits_in_x = set(str(x))
    for digit in str(y):
        if digit not in digits_in_x:
            return False
    return True

n=100 # n cannot be less than 100 (3 digit numbers have 6 permutations, smaller numbers have less)
while True:
    if same_digits(n, n*2) and same_digits(n*2, n*3) and same_digits(n*3, n*4) and same_digits(n*4, n*5) and same_digits(n*5, n*6):
        print(n)
        break
    n+=1

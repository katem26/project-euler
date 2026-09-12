"""If we take 47, reverse and add, 47+74=121, which is palindromic.
Not all numbers produce palindromes so quickly. For example,
349+943=1292
1292+2921=4213
4213+3124=7337
That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise.
In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.

How many Lychrel numbers are there below ten-thousand?"""

def reverse(num):
    r = str(num)[::-1]
    return int(r)

def is_palindromic(num):
    return reverse(num)==num

def lychrel_recurse(num, iterations):
    if iterations > 50:
        return True
    if is_palindromic(num+reverse(num)):
        return False
    return(lychrel_recurse(num+reverse(num), iterations+1))


def solution():
    count = 0
    for n in range(1, 10000):
        if lychrel_recurse(n, 1):
            count+=1
    return count

print("Solution:", solution())


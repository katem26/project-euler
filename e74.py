"""The sum of the factorial of the digits of 145 is equal to 145
1! + 4! + 5! = 145

169 produces a chain of length 3 that links back to itself
    1! + 6! + 9! = 363601
    3! + 6! + 3! + 6! + 0! + 1! = 1454
    1! + 4! + 5! + 4! = 169
    169 -> 363601 -> 1454 (-> 169)

Every starting number will eventually get stuck in a loop. How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

# pre calculating factorials
factorials = [1]
for i in range (1,10):
    next_term = factorials[i-1]*i
    factorials.append(next_term)

def factorial_digit_sum(num):
    total = 0
    string = str(num)
    for digit in string:
        total += factorials[int(digit)]
    return total


loop_lengths = {}
for n in range(1, 1_000_000):
    loop_count = 0
    seen = set()
    a = n
    while a not in seen: # repeat until a repeated term (start of a loop) is found
        # if the next term starts a loop we've already found, we can add its length to the current count to get this number's loop length
        if a in loop_lengths:
            loop_lengths[n] = loop_lengths[a]+loop_count
            break
        else:
            loop_count += 1
            seen.add(a)
            a = factorial_digit_sum(a)
    else: # NB the else block on a while loop runs only when the loop ends normally, not when stopped by a 'break'
        loop_lengths[n] = loop_count

count = 0
for n in loop_lengths:
    if loop_lengths[n] == 60:
        count+=1
print(count)



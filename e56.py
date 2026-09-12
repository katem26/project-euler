# Considering natural numbers of the form a^b, where a, b < 100, what is the maximum digital sum?

def digit_sum(num):
    total = 0
    string = str(num)
    for digit in string:
        total += int(digit)
    return total

maximum=0
for a in range(100):
    for b in range(100):
        c = a**b
        d = digit_sum(c)
        if d > maximum:
            maximum = d
print(maximum)


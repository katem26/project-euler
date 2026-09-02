# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through pandigital.

def isPandigital(number):
    digits = [1,2,3,4,5,6,7,8,9]
    for d in digits:
        if str(d) not in string:
            return False
    return True

totals=[]

# we need to check these ranges as the possible combinations are
# 3 digit x 2 digit = 4 digit and 1 digit x 4 digit = 4 digit
for i in range(1,99):
    for j in range(100,9999):
        num=i*j
        string=str(i)+str(j)+str(num)

        if len(string) != 9:
            continue # we can skip checking if it's not the right length'
        if isPandigital(string):
            print(f"{i}*{j}={num}")
            if num not in totals: # only count unique products
                totals.append(num)

print("sum =", sum(totals))

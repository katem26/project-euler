# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime
# this is pretty slow (runs in 27 seconds), but it does work

concatenated_prime_limit = 100000000
test_prime_limit = 10000

def generator(limit): # prime sieve
    is_prime = [True]*limit
    for x in range (2,limit):
            if is_prime[x] == True:
                # starting at x*2, set all multiples of x to false
                for y in range(x+x,limit,x):
                    is_prime[y] = False
    # after this, the only values that are true are prime (they are not a multiple of any number other than themselves and one)

    primes = []
    for n in range (2,limit): #add all primes to a list
        if is_prime[n] == True:
            primes.append(n)
    return primes


big_prime_set = set(generator(concatenated_prime_limit)) # it's way quicker to check if results are in the set than to run a primality test on each number
def concat_primality_test(num1, num2):
    a = str(num1)
    b = str(num2)
    return int(a+b) in big_prime_set and int(b+a) in big_prime_set # return true if both concatenations are prime e.g. 37 and 73


primes = generator(test_prime_limit)
# create a set of valid pairs
pairs = set()
for p in range(len(primes)):
    for q in range(p, len(primes)):
        if concat_primality_test(primes[p], primes[q]):
            pairs.add((primes[p], primes[q]))


def find_match(prime_list):
    for candidate in primes:
        matches_all = True
        for p in prime_list: # check if the candidate passes the concatenation test for each prime in the list. if so, add it to the list.
            if (p, candidate) not in pairs and (candidate, p) not in pairs:
                matches_all = False
        if matches_all:
            prime_list.append(candidate)
    return prime_list

def solution():
    for prime in primes:
        p = find_match([prime])
        if len(p) >= 5:
            print(p)
            return(sum(p))

print("Solution:", solution())




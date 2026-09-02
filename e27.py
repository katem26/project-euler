# considering quadratics of the form n^2+an+b, where |a| and |b| are <=1000, find the values of a and b that produce the maximum number of primes for consecutive values of n, starting with n=0

def generator(limit): # prime sieve
    is_prime = [True]*limit
    for x in range (2,limit):
            if is_prime[x] == True:
                # starting at x*2, set all multiples of x to false
                for y in range(x+x,limit,x):
                    is_prime[y] = False
    # after this, the only values that are true are prime (they are not a multiple of any number other than themselves and one)

    primes = []
    for n in range (2,len(numbers)): #add all primes to a list
        if is_prime[n] == True:
            primes.append(n)
    return primes


primes = generator(10000)

answer_a=0
answer_b=0
largest_prime_count=0
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        n = 0
        while (n*n)+(a*n)+b in primes:
            n+=1
        if n > largest_prime_count:
            largest_prime_count = n
            answer_a=a
            answer_b=b

print("a =", answer_a)
print("b =", answer_b)
print("number of consecutive primes:", largest_prime_count)

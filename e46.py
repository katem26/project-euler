# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def is_prime(n):
    if n < 2:
        return False
    elif n%2 == 0: # if even
        return False
    else:
        # we only need to check the values up to sqrt(n) because each factor after that multiplies with a factor <=sqrt(n) to make n
        limit = int(n**0.5)
        for i in range(3, limit+1):
            if n%i == 0:
                return False
    return True


def goldbachs(n):
    limit = int(n**0.5) # the square root can't be bigger than sqrt(n)
    for j in range(1, limit+1):
            twice_a_square = 2*j*j
            if is_prime(n-twice_a_square):
                return True
    return False

n = 35
while True:
    if not is_prime(n) and not goldbachs(n):
        print(n)
        break
    n+=2



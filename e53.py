# How many,not necessarily distinct values of nCr for 1<=n<=100 are greater than one-million?

factorials = [1] # pre-compute factorials to save repeating calculations
for i in range(100):
    next_factorial=factorials[i]*(i+1)
    factorials.append(next_factorial)

def combinations(n, r):
    return factorials[n]/(factorials[r]*factorials[n-r])

count = 0
for n in range(100, 0, -1):
    for r in range(100, 0, -1):
        if combinations(n,r)>1e6:
            count+=1

print(count)



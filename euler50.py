# Question: Which prime, below one-million, can be written as the sum of the most consecutive primes
from primesieve import *
from math import *

# Generate list of primes under a million
primes_under_million = generate_primes(10**6)

# Sum of consecutive primes is of order 0.5(n^2)(logn)
# Calculate 'n' so that sum of consecutive primes is less than a million (and not necessarily prime)
nsum = 1
n = 1
while nsum < 10**6:
    nsum = 0.5*(n**2)*(log(n, e))
    n += 1

# Calculate index so that sum of first 'index' consecutive primes is under a million and also prime
primes_subset = primes_under_million[:n]
nsum = sum(primes_under_million[:n])
while nsum > 10**6:
    n -= 1
    nsum = sum(primes_under_million[:n])
primes_sum = 0
index = 0
for i in range(len(primes_subset)):
    if i % 2 == 1:
        pass
    else:
        sumprimes = sum(primes_subset[:i])
        if sumprimes > primes_sum and sumprimes < 10**6 and sumprimes in primes_under_million:
            primes_sum = sumprimes
            index = i

# Print out sum of consecutive primes till 'index', index, n 
print primes_sum, index, n

# Check consecutive primes within a range (index to n) such that their number is greater than index and maximum
j = index + 1
start = 0
while j <= n:
    while (j-start) >= (n-index):
        sumprimes = sum(primes_subset[start:j])
        if sumprimes > primes_sum and sumprimes in primes_under_million:
            primes_sum = sumprimes
        start += 1
    j += 1
    start = 0
print primes_sum
   
        
        
        
        
        
        
        
        

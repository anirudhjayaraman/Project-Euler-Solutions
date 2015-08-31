from primesieve import *
from math import *
def divisors(n):
    limit = int(sqrt(n))
    divisors_list = []
    for i in range(1, limit+1, 1):
        if n % i == 0:
            divisors_list.append(i)
            if i != n/i:
                divisors_list.append(n/i)
    return len(divisors_list)
                

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

n = 100

def sum_of_squares(n):
    return n*(n+1)*(2*n + 1) / 6.0
def square_of_sum(n):
    return (n*(n+1)/2.0)**2
    
print sum_of_squares(100) - square_of_sum(100)

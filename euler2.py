# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fib_list = [1, 2]
limit = 4 * (10**6)
next, sum_even = 0, 2
while next <= limit:
    next = fib_list[-1] + fib_list[-2]
    if next % 2 == 0:
        sum_even += next
    fib_list.append(next)
if fib_list[-1] > limit:
    if fib_list[-1] % 2 == 0:
        sum_even -= fib_list[-1]
    fib_list.pop(-1)
print sum_even
 
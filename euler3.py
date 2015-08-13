# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

x = 600851475143
i = 2
while i < x:
    if x % i == 0:
        x /= i
    else:
        i += 1
print i

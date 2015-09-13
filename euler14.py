# Longest Collatz Sequence under a million
# Function listing collatz sequence for a number
def collatz(n):
    "function listing collatz sequence for a positive integer"
    coll = []
    coll.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n/2
            coll.append(n)
        else:
            n = 3*n + 1
            coll.append(n)
    return coll
    
longest = 0
j = 0
for i in xrange(1, 1000000):
    lencoll = len(collatz(i))
    if lencoll > longest:
        longest = lencoll
        j = i
print j
        

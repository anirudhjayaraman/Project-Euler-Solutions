collatz = {1:1}
def Collatz(n):
    global collatz
    if not collatz.has_key(n):
        if n%2 == 0:
            collatz[n] = Collatz(n/2) + 1
        else:
            collatz[n] = Collatz(3*n + 1) + 1
    return collatz[n]

for j in range(1000000,0,-1):
    Collatz(j)

print collatz.keys()[collatz.values().index(max(collatz.values()))] 

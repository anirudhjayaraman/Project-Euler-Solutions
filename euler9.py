# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# a**2 + b**2 = c**2


for a in range(1000):
    for b in range(1000):
        if a**2 + b**2 == (1000 - a - b)**2 and a > 0 and b > 0 and (1000 - a - b) > 0:
            x = a
            y = b
            z = 1000 - a - b
            break
if x + y + z == 1000:
    print x, y, z
    print x*y*z

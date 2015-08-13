a, b = 999, 999

def isPalindrome(x):
    if len(str(x)) == 1:
        return True
    mid = len(str(x))//2
    x_str = str(x)
    for i in range(mid + 1):
        if x_str[i] != x_str[-i - 1]:
            return False
    return True

palindrome = 0
for a in range(999, 100, -1):
    for b in range(999, 100, -1):
        prod = a * b
        if isPalindrome(prod):
            if prod > palindrome:
                palindrome = prod
print palindrome 
 


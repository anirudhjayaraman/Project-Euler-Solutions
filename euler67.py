# Read the problem matrix into a triangle array in python
filename = 'euler67.txt'
with open(filename, "r") as ins:
    array = []
    for line in ins:
        array.append(line)
# Convert the triangle arry entries into integers
newArray = []
for i in array:
    j = i.split(' ')
    k = [int(n) for n in j]
    newArray.append(k)
l = len(newArray)
# Algorithm to calculate Maximum Path Sum
for i in range(l-1):
    array1 = newArray[-1]
    array2 = newArray[-2]
    for j in range(len(array2)):
        array2[j] += max(array1[j], array1[j+1])
    newArray.pop(-1)
    newArray[-1] = array2
print newArray[0][0]   

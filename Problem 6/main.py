import math

def squareSum(limit):
    sum = 0
    for x in range(1,limit+1):
        sum += x
    return math.pow(sum, 2)
        
def sumSquare(limit):
    sum = 0
    for x in range(1, limit+1):
        sum += math.pow(x, 2)
    return sum

print(squareSum(100) - sumSquare(100))
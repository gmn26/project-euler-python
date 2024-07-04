numb = 600851475143
divider = 2

def check_prime(numb):
    if numb == 1:
        return True
    i = 2
    while i < numb:
        if numb % i == 0:
            return False
        i += 1
    return True

while not check_prime(numb) :
    if check_prime(divider):
        if numb % divider == 0:
            numb /= divider
        else:
            divider += 1
    else:
        divider += 1
            
print(numb)

# 60
# 2 * 30a
# 2 * 2 * 15
# 2 * 2 * 3 * 5

def smallestMultiple(numb):
    counter = 0
    for x in range(1,21):
        if((numb % x) == 0):
            counter += 1
    if(counter == 20):
        return True
    return False
        
numb = 21
while smallestMultiple(numb) == False:
    numb += 1
    
print(numb)
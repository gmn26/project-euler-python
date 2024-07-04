def checkPalindrom(numb):
    palimStat = False
    palimCounter = 0
    numb_list = [int(digit) for digit in str(numb)]
    for x in range(len(numb_list)//2):
        if(numb_list[x] == numb_list[len(numb_list)-(x+1)]):
            palimCounter+=1
    if(palimCounter == len(numb_list)//2):
        palimStat = True
    return palimStat
        
highestPalin = 0
                
for x in range(100, 1000):
    for y in  range(x, 1000):
        numb = x * y
        if(checkPalindrom(numb) and numb>highestPalin):
            highestPalin = numb
        
print(highestPalin)
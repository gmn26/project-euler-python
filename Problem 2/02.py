fibb = [1, 2]
numb = 0
result = 2
# print(fibb[0] , ", " , fibb[1] , ", " , end=" ")

while fibb[1] < 4000000:
    numb = fibb[0] + fibb[1]
    fibb[0] = fibb[1]
    fibb[1] = numb
    # print(numb , ", " , end=" ")
    if (numb % 2 == 0):
        result += numb
        
print("Hasil adalah : ", result)
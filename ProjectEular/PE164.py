total = 0
currentN = 1000000000
while currentN != 9999999999:
    P = 0
    for i in str(currentN):
        currentN = str(currentN)
        if P == 7:
            break
        sum = int(i) + int(currentN[P+1]) + int(currentN[P+2])
        if sum <= 9:
            total += 1
        P =+ 1
    currentN = int(currentN)
    currentN += 1
    #print(currentN)
print(total)
top = 99
S = [20 ,1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5]
D = [40, 2, 36, 8, 26, 12, 20, 30, 4, 34, 6, 38, 14, 32, 16, 22, 28, 18, 24, 10]
T = [40, 2, 36, 8, 26, 12, 20, 30, 4, 34, 6, 38, 14, 32, 16, 22, 28, 18, 24, 10]
IB = 50 ##Inner bulls eye
OB = 25 ##Outer bulls eye

total = 0

#Loop through all numbers less than 100
for score in range(2,top+1):
    ## MMV
    for dart_3 in D:
        if score == dart_3:
            total += 1
    
    ## MVV
    for dart_2 in S:
        if dart_2 < score:
            tempScore = score
            tempScore -= dart_2
            for dart_3 in D:
                if tempScore == dart_3:
                    total += 1


print(total)
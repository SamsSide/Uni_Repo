k = int(input("Input k"))
for x in range(2,k-1):
    if k % x == 0:
        exit()
print("Prime")

ARR = [1,2,9,8,6,6,4,5,6,8,52,6,4,6,8,5,4,5,0,6,7,6]

ELE = int(input("Enter element to search"))

for i in range(len(ARR)):
    if ARR[i] == ELE:
        print(ELE , " found at index ", i)
        exit(0)
print(ELE, " not found in array")
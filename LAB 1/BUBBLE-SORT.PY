ARR = [1,2,9,8,6,6,4,5,6,8,52,6,4,6,8,5,4,5,0,6,7,6]

n = len(ARR)

for i in range(n):
    for j in range(0,n-i-1):
        if ARR[j] > ARR[j+1]:
            ARR[j] , ARR[j+1] = ARR[j+1] , ARR[j]
print(ARR)
arr = [1,2,3,4,5,3,3,1]
dublicates = []
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            if arr[i] not in dublicates:
                dublicates.append(arr[i])
print(dublicates)
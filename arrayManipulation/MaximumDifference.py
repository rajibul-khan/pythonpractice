arr = [7, 1, 5, 3, 6, 4]
max_difference = arr[1] - arr[0]
for i in range(len(arr)):
    for j in range(i+i,len(arr)):
        difference = arr[j]-arr[i]
        if max_difference < difference:
            max_difference = difference
print(max_difference)
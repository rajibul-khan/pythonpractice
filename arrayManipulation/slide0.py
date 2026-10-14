arr = [0, 1, 0, 3, 12]
newarr=[]
for i in range(len(arr)):
    if arr[i]==0:
        arr.append(arr[i])
        arr.pop(i)
print(arr)
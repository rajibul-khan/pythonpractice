arr = [1,2,3 ,4,5]
is_sort= True
for i in range(len(arr)- 1):
    if arr[i] > arr[ i+1]:
        is_sort = False
print(is_sort)
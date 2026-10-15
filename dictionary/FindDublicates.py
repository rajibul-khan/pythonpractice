numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 3]
frequency ={}
for num in numbers:
    frequency[num]=frequency.get(num,0)+1

dublicate = {
    number: count
    for number, count in frequency.items()
    if count >1
}

print(dublicate)

#non repeating char
for num in numbers:
    if frequency[num]== 1:
        print(num)
        break
else:
    print("no non repeatin char")
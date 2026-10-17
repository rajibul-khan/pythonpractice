numbers = [2, 31, 11, 7]
target = 9

seen ={}
answer = None
for index , num in enumerate(numbers):
    needed = target - num
    if needed in seen:
        answer = [seen[needed],index]
        break
    seen[num]= index
print(answer)
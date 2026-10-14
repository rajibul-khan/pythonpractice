a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common= []
for num in a:
    for other in b:
        if num == other:
            if num not in common:
                common.append(num)
print(common)
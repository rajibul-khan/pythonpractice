words = [
    "apple",
    "ant",
    "banana",
    "ball",
    "cat",
    "car"
]
group ={}
for word in words:
    firstLetter  = word[0]
    if firstLetter not in group:
        group[firstLetter] = []
    group[firstLetter].append(word)
print(group)
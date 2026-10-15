text = "programing"
frequency ={}
for char in text:
    if char in frequency:
        frequency[char]+= 1
    else:
        frequency[char] = 1
print(frequency)

  #word count

freq ={}
sentence = "python is easy and python is powerful"
words = sentence.split()
for word in words:
    freq[word] = freq.get(word,0)+1
print(freq)
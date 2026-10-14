scores = {
    "Rajibul": 85,
    "Rahul": 72,
    "Aman": 91
}
print(scores.keys())
print(scores.values())
print(scores.items())
    #looping through dict 
for key in scores:
    print (key, " scores is ",scores[key])

    #useing get()
print(scores.get("Rajibul"))
print(scores.get("phone", "not provided"))
 # setdefault
newdict = scores.copy()
newdict["Rajibul"]= 100
print(newdict.items())
scores.clear()
print(scores)
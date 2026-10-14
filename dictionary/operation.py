marks = {
    "Math": 80,
    "Science": 90,
    "English": 70,
    "Computer": 95
}
total =(sum(marks.values()))
print(total/4)
print(total)
 #using a loop 
Max  =0 
for value in marks.values():
   Max += value

print(Max)
print(Max/len(marks))
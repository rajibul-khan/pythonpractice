students = {
    "student1": {
        "name": "Rajibul",
        "age": 21,
        "marks": 85
    },
    "student2": {
        "name": "rahul", 
        "age" : 23,
        "marks": 22
        
    }
}
#print rajibul marks
print(students["student1"]['name'])

 #update rahul marks
students["student2"]["marks"] = 100

#add aman

students["student3"]= {
    "name":"aman",
    "age": 24,
    "marks": 15

}

#display all student
for student_id , detail in students.items():
    print(student_id,detail["name"],detail["marks"])
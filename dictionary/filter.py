students = {
    "Rajibul": 85,
    "Rahul": 45,
    "Aman": 92,
    "John": 38,
    "Sara": 76
}
Pass = {}
for name , mark in students.items():
    if mark >= 60:
        Pass[name] = mark
print(Pass)

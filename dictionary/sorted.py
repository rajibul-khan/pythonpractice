scores = {
    "Rajibul": 85,
    "Rahul": 72,
    "Aman": 91,
    "John": 65
}
sort = dict(
    sorted(
        scores.items(),
        key=lambda x:x[1],
        reverse= True
    )
)
print(sort)
sales = {
    "Monday": 1200,
    "Tuesday": 1800,
    "Wednesday": 900,
    "Thursday": 2200
}
highest_day  = lowest_day  = None
highest_sale = float('-inf')
lowest_sale = float('inf')
for day,amount in sales.items():
    if amount >highest_sale:
        highest_sale = amount
        highest_day =day
    if amount < lowest_sale:
        lowest_sale = amount
        lowest_day = day 
#print(highest_day,highest_sale)
#print(lowest_day, lowest_sale)



print(max(sales.values()))
print(min(sales.values()))
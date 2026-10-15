dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}
merged  = dict1 | dict2
print(merged)

dict1 = {"a": 10, "b": 20}
dict2 = {"b": 99, "c": 30}
merger = {**dict1,**dict2}
print(merger)
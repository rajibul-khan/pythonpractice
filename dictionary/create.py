dict = {
   "name":"rajibul", 
    'age':22, 
    'profession':"data analyst"
}
print(dict["age"])
#add new values 
dict['course']="computer science"
#update existing value
dict["age"]= 24
print(dict)

 # delete  a key in dict
dict.pop('age')

print(dict)
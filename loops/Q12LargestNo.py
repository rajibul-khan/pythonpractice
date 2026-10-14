#largest from user input
numbers = list(map(int, input("Enter multiple numbers: ").split()))
max = 0
for  i in numbers:
    if i >= max:
        max = i 
print(max)

#smallest  no.
small = i
for i in numbers:

    if i <=small:
        small= i
print(small)
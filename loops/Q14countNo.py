n = int(input('enter no. : '))
count = 0 
if n == 0: 
    count+=1
else:
    n = abs(n)
    while n> 0 : 
        count +=1
        n //=10
print(count)
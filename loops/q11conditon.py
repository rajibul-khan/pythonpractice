#print no between 1 to 100 that are divisible by 3 and 5 both 
for i in range(1,101):
    if i%3==0 and i%5 ==0:
        print(i)
#count no divisible by 7 from 1 to 100
count= 0
for i in range(1,101):
    if i % 7 == 0:
        count += 1


print(count)
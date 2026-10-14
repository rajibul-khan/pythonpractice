n = int(input('enter no : '))
total = 0
while n> 0:
    digit = n%10 
    total += digit
    n //= 10
print(total)


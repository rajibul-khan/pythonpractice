n = int(input('enter no : '))
Max =0
while n >0 :
    digit = n%10
    if Max < digit: 
        Max = digit
    n //= 10
print(Max)
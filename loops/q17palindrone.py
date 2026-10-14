n = int(input('enter no ; '))
original = n 
reverse = 0
while n>0: 
    digit  = n%10
    reverse = reverse * 10 +digit
    n //= 10
if original >= 0 and original == reverse:
    print('palindrome')
else:
    print('not a palindrome')
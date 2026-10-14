
#12345
#12345
#12345
#12345
#12345
for i in range(1,6):
    print(*range(1,6))

# print a square
for i in range(1,6):
    for i in range(1,6):
        print("*", end= "")
    print()
# print a hollow square
size = 5
for i in range(size):
    for j in range(size):
        if i == 0 or i== size-1 or j ==0 or j == size -1:
            print('*',end=" ")
        else:
            print(' ', end=" ")
    print()
#print triangle
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
#print reverse triangle
for  i  in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
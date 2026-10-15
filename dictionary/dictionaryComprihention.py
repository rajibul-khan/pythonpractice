# dictionary of sqaure 
square = {
    number:number**2
    for number in range(1,11)

}
print(square)

#dict with filters

cube_of_even = {
    number: number**3
    for number in range(1,11)
    if number%2 == 0
}
print(cube_of_even)
#This program lets you add products, update stock, sell products, display out-of-stock products, and calculate total inventory.
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}
def add_product(product,quantity):
    if quantity< 0:
        print("Invalid Quantity")
        return
    inventory[product] = inventory.get(product,0) + quantity
    print(product,"add successfully")
print("modes ")
print("1. add product")
n = int(input("enter mode "))
if n == 1:
    i = input("enter product ")
    j = int(input("enter quantity "))
    add_product(i,j)

def sellProduct(product,quantity):
    if quantity<0:
        print('enter valid quantity')
    elif product not in inventory:
        print('product not in store')
    elif inventory[product] <quantity:
        print('insufficient stock')
    else:
        inventory[product]-= quantity
        print('sale complete')

# list product out of stock
def outOffStock():
    for name,value in inventory.items():
        if value == 0:
            print(name)
    
# total number of inventory 
def total():
    print(sum(inventory.values()))


    return sum(inventory.values())


add_product("apple", 5)
add_product("mango", 12)

sellProduct("banana", 3)
sellProduct("orange", 20)

print("Inventory:", inventory)
print("Total items:", total())

print("Out of stock:")
outOffStock()
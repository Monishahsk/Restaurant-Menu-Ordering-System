#define the menuof restaurant
menu={
    "Pizza":50,
    "Pasta":45,
    "Burger":60,
    "Cold Coffee":90,
    "Salad":70,
}

#Great
print("Welcome to PriyaShree Restaurent")
print("Pizza: Rs50\nPasta: Rs45\nBurger: Rs60\nCold Coffee: Rs90\nSalad: Rs70")

order_total=0
#60+50=110 #used to store total cost of ordered item/items

item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item is added to your order")
else:
    print(f"Please order something else this item is not available here")
another_order = input("Do you want to order anything else? (Yes/No):")
if another_order =="Yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} is added to your order")
    else:
        print("Order item {item_2} is not avaialble!")
print(f"The total amount of items to pay is {order_total}")
print("THANK YOU  for visiting PS restaurent") 
print("HAVE A GREAT DAY AHEAD")         
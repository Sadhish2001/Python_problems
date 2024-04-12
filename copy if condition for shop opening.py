print("Welcome to Pizza Hut")

print("Choose your Pizza")

print("1. Veg Pizza")

print("2. Non veg Pizza")

user = int(input("Please choose your menu: "))

print("1. Onion Pizza")

print("2. Tomato Pizza")

print("3. Capsicum Pizza")

print("4. Mushroom Pizza")

print("5. Paneer Pizza")

print("6. Chicken Cheese Pizza")

print("7. Chicken Mexican Pizza")

print("8. Chicken Tikka Pizza")

print("9. BBQ Chicken Pizza")

print("10. spicy Chicken Pizza")

user = int(input("Please choose your menu: "))

price = 0

OnionPizza = 100
TomatoPizza = 120
CapsicumPizza = 200
MushroomPizza = 250
PaneerPizza = 290
ChickenCheesePizza = 320
ChickenMexicanPizza = 360
ChickenTikkaPizza = 380
BBQChickenPizza = 400
spicyChickenPizza = 450
extracheese = 20
extratoppings = 40
cheeseburst = 60

if user == 1:
    addExtraCheese = input("Do you want to add Extra Cheese: Y/N:")
    addExtraToppings = input("Do you want to add Extra Toppings: Y/N:")
    addCheeseBurst = input("Do you want to add more Cheese Burst: Y/N:")
    price += OnionPizza
    if addExtraCheese == "Y":
        price += extracheese
        print(f"Extra Cheese price: ₹{extracheese}")
    if addExtraToppings == "Y":
        price += extratoppings
        print(f"Extra Toppings price: ₹{extratoppings}")
    if addCheeseBurst == "Y":
        price += cheeseburst
        print(f"Extra Cheese Burst price: ₹{cheeseburst}")

    print(f"Onion Pizza price: ₹{OnionPizza}")
    print(f"Your total amount: ₹{price}")




# print("Welcome to StarBucks😀")

# print("1. Latte")

# print("2. Cappuccino")

# print("3. Ice cream")

# user = int(input("Please choose your menu: "))

# price = 0

# latte = 200
# cappuccino = 350
# blackcurrent = 50
# chocolate = 40
# vanilla = 30
# sugar = 20
# cream = 30

# if user == 1:
#     addSugar = input("Do you want to add more sugar: Y/N")
#     addCream = input("Do you want strong: Y/N")
#     price += latte
#     if addSugar == "Y":
#         price += sugar
#         print(f"sugar price: ₹{sugar}")
#     if addCream == "Y":
#         price += cream
#         print(f"cream price: ₹{cream}")

#     print(f"latte price: ₹{latte}")
#     print(f"Your total amount: ₹{price}")

# elif user == 2:
#     addSugar = input("Do you want to add more sugar: Y/N")
#     addCream = input("Do you want strong: Y/N")
#     price += cappuccino
#     if addSugar == "Y":
#         price += sugar
#         print(f"sugar price: ₹{sugar}")
#     if addCream == "Y":
#         price += cream
#         print(f"cream price: ₹{cream}")

#     print(f"latte price: ₹{cappuccino}")
#     print(f"Your total amount: ₹{price}")


# elif user == 3:
#     print("1. blackcurrent")
#     print("2. chocolate")
#     print("3. vanilla")
#     flavour = int(input("What flavour do you want: "))
#     if flavour == 1:
#         price += blackcurrent
#         print(f"blackcurrent price: ₹{blackcurrent}")
#     if flavour == 2:
#         price += chocolate
#         print(f"chocolate price: ₹{chocolate}")
#     if flavour == 3:
#         price += vanilla
#         print(f"vanilla price: ₹{vanilla}")

#     print(f"Your total amount: ₹{price}")

# else:
#     print("Invalid input")
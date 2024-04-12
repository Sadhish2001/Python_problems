print("Welcome to Pizza Hut")
print("Choose your Pizza")
print("1. Onion Pizza")
print("2. Tomato Pizza")
print("3. Capsicum Pizza")
print("4. Mushroom Pizza")
print("5. Paneer Pizza")
print("6. Chicken Cheese Pizza")
print("7. Chicken Mexican Pizza")
print("8. Chicken Tikka Pizza")
print("9. BBQ Chicken Pizza")
print("10. Spicy Chicken Pizza")
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
SpicyChickenPizza = 450
ExtraCheese = 20
ExtraToppings = 40
CheeseBurst = 60

if user == 1:
    addExtraCheese = input("Do you want Extra Cheese: Y/N :")
    addExtraToppings = input("Do you want Extra Toppings: Y/N :")
    addCheeseBurst = input("Do you want Cheese Burst: Y/N :")
    price += OnionPizza
    if addExtraCheese == "Y":
        price += ExtraCheese
        print(f"Extra Cheese price: ₹{ExtraCheese}")
    if addExtraToppings == "Y":
        price += ExtraToppings
        print(f"Extra Toppings price: ₹{ExtraToppings}")
    if addCheeseBurst == "Y":
        price += CheeseBurst
        print(f"Cheese Burst price: ₹{CheeseBurst}")    
    print(f"onion Pizza price: ₹{OnionPizza}")
    print(f"Your total amount: ₹{price}")


elif user == 2:
    addExtraCheese = input("Do you want Extra Cheese: Y/N :")
    addExtraToppings = input("Do you want Extra Toppings: Y/N :")
    addCheeseBurst = input("Do you want Cheese Burst: Y/N :")
    price += TomatoPizza
    if addExtraCheese == "Y":
        price += ExtraCheese
        print(f"Extra Cheese price: ₹{ExtraCheese}")
    if addExtraToppings == "Y":
        price += ExtraToppings
        print(f"Extra Toppings price: ₹{ExtraToppings}")
    if addCheeseBurst == "Y":
        price += CheeseBurst
        print(f"Cheese Burst price: ₹{CheeseBurst}")   
    print(f"Tomato Pizza price: ₹{TomatoPizza}")
    print(f"Your total amount: ₹{price}")
    
elif user == 3:
    addExtraCheese = input("Do you want Extra Cheese: Y/N :")
    addExtraToppings = input("Do you want Extra Toppings: Y/N :")
    addCheeseBurst = input("Do you want Cheese Burst: Y/N :")
    price += CapsicumPizza
    if addExtraCheese == "Y":
        price += ExtraCheese
        print(f"Extra Cheese price: ₹{ExtraCheese}")
    if addExtraToppings == "Y":
        price += ExtraToppings
        print(f"Extra Toppings price: ₹{ExtraToppings}")
    if addCheeseBurst == "Y":
        price += CheeseBurst
        print(f"Cheese Burst price: ₹{CheeseBurst}")   
    print(f"Capsicum Pizza price: ₹{CapsicumPizza}")
    print(f"Your total amount: ₹{price}")
    
elif user == 4:
    addExtraCheese = input("Do you want Extra Cheese: Y/N :")
    addExtraToppings = input("Do you want Extra Toppings: Y/N :")
    addCheeseBurst = input("Do you want Cheese Burst: Y/N :")
    price += MushroomPizza
    if addExtraCheese == "Y":
        price += ExtraCheese
        print(f"Extra Cheese price: ₹{ExtraCheese}")
    if addExtraToppings == "Y":
        price += ExtraToppings
        print(f"Extra Toppings price: ₹{ExtraToppings}")
    if addCheeseBurst == "Y":
        price += CheeseBurst
        print(f"Cheese Burst price: ₹{CheeseBurst}")   
    print(f"Mushroom Pizza price: ₹{MushroomPizza}")
    print(f"Your total amount: ₹{price}")
    
elif user == 5:
    addExtraCheese = input("Do you want Extra Cheese: Y/N :")
    addExtraToppings = input("Do you want Extra Toppings: Y/N :")
    addCheeseBurst = input("Do you want Cheese Burst: Y/N :")
    price += PaneerPizza
    if addExtraCheese == "Y":
        price += ExtraCheese
        print(f"Extra Cheese price: ₹{ExtraCheese}")
    if addExtraToppings == "Y":
        price += ExtraToppings
        print(f"Extra Toppings price: ₹{ExtraToppings}")
    if addCheeseBurst == "Y":
        price += CheeseBurst
        print(f"Cheese Burst price: ₹{CheeseBurst}")      
    print(f"Paneer Pizza price: ₹{PaneerPizza}")
    print(f"Your total amount: ₹{price}")
    
elif user == 6:
    addExtraCheese = input("Do you want Extra Cheese: Y/N :")
    addExtraToppings = input("Do you want Extra Toppings: Y/N :")
    addCheeseBurst = input("Do you want Cheese Burst: Y/N :")
    price += ChickenCheesePizza
    if addExtraCheese == "Y":
        price += ExtraCheese
        print(f"Extra Cheese price: ₹{ExtraCheese}")
    if addExtraToppings == "Y":
        price += ExtraToppings
        print(f"Extra Toppings price: ₹{ExtraToppings}")
    if addCheeseBurst == "Y":
        price += CheeseBurst
        print(f"Cheese Burst price: ₹{CheeseBurst}")   
    print(f"Chicken Cheese Pizza price: ₹{ChickenCheesePizza}")
    print(f"Your total amount: ₹{price}")
    
elif user == 7:
    addExtraCheese = input("Do you want Extra Cheese: Y/N :")
    addExtraToppings = input("Do you want Extra Toppings: Y/N :")
    addCheeseBurst = input("Do you want Cheese Burst: Y/N :")
    price += ChickenMexicanPizza
    if addExtraCheese == "Y":
        price += ExtraCheese
        print(f"Extra Cheese price: ₹{ExtraCheese}")
    if addExtraToppings == "Y":
        price += ExtraToppings
        print(f"Extra Toppings price: ₹{ExtraToppings}")
    if addCheeseBurst == "Y":
        price += CheeseBurst
        print(f"Cheese Burst price: ₹{CheeseBurst}")    
    print(f"Chicken Mexican Pizza price: ₹{ChickenMexicanPizza}")
    print(f"Your total amount: ₹{price}")
    
elif user == 8:
    addExtraCheese = input("Do you want Extra Cheese: Y/N :")
    addExtraToppings = input("Do you want Extra Toppings: Y/N :")
    addCheeseBurst = input("Do you want Cheese Burst: Y/N :")
    price += ChickenTikkaPizza
    if addExtraCheese == "Y":
        price += ExtraCheese
        print(f"Extra Cheese price: ₹{ExtraCheese}")
    if addExtraToppings == "Y":
        price += ExtraToppings
        print(f"Extra Toppings price: ₹{ExtraToppings}")
    if addCheeseBurst == "Y":
        price += CheeseBurst
        print(f"Cheese Burst price: ₹{CheeseBurst}")    
    print(f"Chicken Tikka Pizza price: ₹{ChickenTikkaPizza}")
    print(f"Your total amount: ₹{price}")
    
elif user == 9:
    addExtraCheese = input("Do you want Extra Cheese: Y/N :")
    addExtraToppings = input("Do you want Extra Toppings: Y/N :")
    addCheeseBurst = input("Do you want Cheese Burst: Y/N :")
    price += BBQChickenPizza
    if addExtraCheese == "Y":
        price += ExtraCheese
        print(f"Extra Cheese price: ₹{ExtraCheese}")
    if addExtraToppings == "Y":
        price += ExtraToppings
        print(f"Extra Toppings price: ₹{ExtraToppings}")
    if addCheeseBurst == "Y":
        price += CheeseBurst
        print(f"Cheese Burst price: ₹{CheeseBurst}")    
    print(f"BBQ Chicken Pizza price: ₹{BBQChickenPizza}")
    print(f"Your total amount: ₹{price}")
    
elif user == 10:
    addExtraCheese = input("Do you want Extra Cheese: Y/N :")
    addExtraToppings = input("Do you want Extra Toppings: Y/N :")
    addCheeseBurst = input("Do you want Cheese Burst: Y/N :")
    price += SpicyChickenPizza
    if addExtraCheese == "Y":
        price += ExtraCheese
        print(f"Extra Cheese price: ₹{ExtraCheese}")
    if addExtraToppings == "Y":
        price += ExtraToppings
        print(f"Extra Toppings price: ₹{ExtraToppings}")
    if addCheeseBurst == "Y":
        price += CheeseBurst
        print(f"CheeseBurst price: ₹{CheeseBurst}")
    print(f"spicy Chicken Pizza price: ₹{SpicyChickenPizza}")
    print(f"Your total amount: ₹{price}")

else:
    print("Invalid input")
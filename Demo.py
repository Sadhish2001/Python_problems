# for i in range(1, 5+1):  
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i*j}")
#     print()
    
# num = int(input("sum of natural numbers : "))
# sum = 0

# for i in range(1, num + 1):
#     if(not (i % 2) == 0):
#         sum += i
    
# print("\nSum of odd numbers from 1 to", num, "is :", sum)

      
      
# if user == 2:
#     print("1. Chicken Cheese Pizza")
#     print("2. Chicken Mexican Pizza")
#     print("3. Chicken Tikka Pizza")
#     print("4. BBQ Chicken Pizza")
#     print("5. spicy Chicken Pizza")

#     user = int(input("Please choose your menu: "))
  
#     if user == 1:
#         ExtraCheese = input("Do you want Extra Cheese: Y/N :")
#         ExtraToppings = input("Do you want Extra Toppings: Y/N :")
#         CheeseBurst = input("Do you want Cheese Burst: Y/N :")
#         price += ChickenCheesePizza
#     if ExtraCheese == "Y":
#         price += ExtraCheese
#         print(f"Extra Cheese price: ₹{ExtraCheese}")
#         print(f"Chicken Cheese Pizza price: ₹{ChickenCheesePizza}")
#         print(f"Your total amount: ₹{price}")
#     if ExtraToppings == "Y":
#         price += ExtraToppings
#         print(f"Extra Toppings price: ₹{ExtraToppings}")
#         print(f"Chicken Cheese Pizza price: ₹{ChickenCheesePizza}")
#         print(f"Your total amount: ₹{price}")
#     if CheeseBurst == "Y":
#         price += CheeseBurst
#         print(f"CheeseBurst price: ₹{CheeseBurst}") 
#         print(f"Chicken Cheese Pizza price: ₹{ChickenCheesePizza}")
#         print(f"Your total amount: ₹{price}")
    
#     elif user == 2:
#         ExtraCheese = input("Do you want Extra Cheese: Y/N :")
#         ExtraToppings = input("Do you want Extra Toppings: Y/N :")
#         CheeseBurst = input("Do you want Cheese Burst: Y/N :")
#         price += ChickenMexicanPizza
#         if ExtraCheese == "Y":
#             price += ExtraCheese
#             print(f"Extra Cheese price: ₹{ExtraCheese}")
#             print(f"Chicken Mexican Pizza price: ₹{ChickenMexicanPizza}")
#             print(f"Your total amount: ₹{price}")
#         if ExtraToppings == "Y":
#             price += ExtraToppings
#             print(f"Extra Toppings price: ₹{ExtraToppings}")
#             print(f"Chicken Mexican Pizza price: ₹{ChickenMexicanPizza}")
#             print(f"Your total amount: ₹{price}")
#         if CheeseBurst == "Y":
            
#             price += CheeseBurst
#             print(f"CheeseBurst price: ₹{CheeseBurst}")
#             print(f"Chicken Mexican Pizza price: ₹{ChickenMexicanPizza}")
#             print(f"Your total amount: ₹{price}")
    
#     elif user == 3:
#         ExtraCheese = input("Do you want Extra Cheese: Y/N :")
#         ExtraToppings = input("Do you want Extra Toppings: Y/N :")
#         CheeseBurst = input("Do you want Cheese Burst: Y/N :")
#         price += ChickenTikkaPizza
#         if ExtraCheese == "Y":
#             price += ExtraCheese
#             print(f"Extra Cheese price: ₹{ExtraCheese}")
#             print(f"BBQ Chicken Pizza price: ₹{BBQChickenPizza}")
#             print(f"Your total amount: ₹{price}")
#         if ExtraToppings == "Y":
#             price += ExtraToppings
#             print(f"Extra Toppings price: ₹{ExtraToppings}")
#             print(f"BBQ Chicken Pizza price: ₹{BBQChickenPizza}")
#             print(f"Your total amount: ₹{price}")
#         if CheeseBurst == "Y":
#             price += CheeseBurst
#             print(f"CheeseBurst price: ₹{CheeseBurst}")
#             print(f"Chicken Tikka Pizza price: ₹{ChickenTikkaPizza}")
#             print(f"Your total amount: ₹{price}")
    
#     elif user == 4:
#         ExtraCheese = input("Do you want Extra Cheese: Y/N :")
#         ExtraToppings = input("Do you want Extra Toppings: Y/N :")
#         CheeseBurst = input("Do you want Cheese Burst: Y/N :")
#         price += BBQChickenPizza
#         if ExtraCheese == "Y":
#             price += ExtraCheese
#             print(f"Extra Cheese price: ₹{ExtraCheese}")
#             print(f"BBQ Chicken Pizza price: ₹{BBQChickenPizza}")
#             print(f"Your total amount: ₹{price}")
#         if ExtraToppings == "Y":
#             price += ExtraToppings
#             print(f"Extra Toppings price: ₹{ExtraToppings}")
#             print(f"BBQ Chicken Pizza price: ₹{BBQChickenPizza}")
#             print(f"Your total amount: ₹{price}")
#         if CheeseBurst == "Y":
#             price += CheeseBurst
#             print(f"CheeseBurst price: ₹{CheeseBurst}")
#             print(f"BBQ Chicken Pizza price: ₹{BBQChickenPizza}")
#             print(f"Your total amount: ₹{price}")
    
#     elif user == 5:
#         ExtraCheese = input("Do you want Extra Cheese: Y/N :")
#         ExtraToppings = input("Do you want Extra Toppings: Y/N :")
#         CheeseBurst = input("Do you want Cheese Burst: Y/N :")
#         price += spicyChickenPizza
#         if ExtraCheese == "Y":
#             price += ExtraCheese
#             print(f"Extra Cheese price: ₹{ExtraCheese}")
#             print(f"BBQ Chicken Pizza price: ₹{BBQChickenPizza}")
#             print(f"Your total amount: ₹{price}")
#         if ExtraToppings == "Y":
#             price += ExtraToppings
#             print(f"Extra Toppings price: ₹{ExtraToppings}")
#             print(f"BBQ Chicken Pizza price: ₹{BBQChickenPizza}")
#             print(f"Your total amount: ₹{price}")
#         if CheeseBurst == "Y":
#             price += CheeseBurst
#             print(f"CheeseBurst price: ₹{CheeseBurst}")
#             print(f"spicy Chicken Pizza price: ₹{spicyChickenPizza}")
#             print(f"Your total amount: ₹{price}")

# num = float(input("Enter a number: "))
# if num > 0:
#    print("Positive number")
# elif num == 0:
#    print("Zero")
# else:
#    print("Negative number")



# number = int(input("Enter a Number : "))

# if((number % 5 == 0) and (number % 11 == 0)):
#     print("Number is Divisible by 5 and 11".format(number))
# else:
#     print("Number is Not Divisible by 5 and 11".format(number)) 



#num = int(input("Enter a number: "))
#if (num % 2) == 0:
   #print("{0} is Even".format(num))
#else:
   #print("{0} is Odd".format(num))



#yr = int(input("Enter the Year: "))

#if (( yr%400 == 0) or (( yr%4 == 0 ) and ( yr%100 != 0))):
 #   print("is a Leap year")
#else:
    #print("is Not a Leap year")



#ch = input("Enter the Character : ")

#if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
 #   print("The Character ", ch, "is an Alphabet")
#else:
 #   print("The Character ", ch, "is Not an Alphabet")


# ch = input("Please Enter Your Own Character : ")

# if(ch.isalpha()):
#     print("The Given Character ", ch, "is an Alphabet")
# else:
#     print("The Given Character ", ch, "is Not an Alphabet")



# ch = input("Enter a character: ")

# if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
#  or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
#     print(ch, "is a Vowel")
# else:
#     print(ch, "is not a Vowely ")



# ch = input("Please Enter Your Own Character : ")

# if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
#     print("The Given Character ", ch, "is an Alphabet") 
# elif(ch >= '0' and ch <= '9'):
#     print("The Given Character ", ch, "is a Digit")
# else:
#     print("The Given Character ", ch, "is a Special Character")


# ch = input("Enter a Character : ")

# if(ch.isupper()):
#     print("The Given Character ", ch, "is an Uppercase Alphabet")
# elif(ch.islower()):
#     print("The Given Character ", ch, "is a Lowercase Alphabet")
# else:
#     print("The Given Character ", ch, "is Not a Lower or Uppercase Alphabet")



# weekday = int(input("Enter weekday number (1-7) : "))

# if weekday == 1 :
#     print("\nMonday");

# elif weekday == 2 :
#     print("\nTuesday")

# elif(weekday == 3) :
#     print("\nWednesday")

# elif(weekday == 4) :
#     print("\nThursday")

# elif(weekday == 5) :
#     print("\nFriday")

# elif(weekday == 6) :
#     print("\nSaturday")

# elif (weekday == 7) :
#     print("\nSunday")

# else :
#     print("\nPlease enter any weekday number (1-7)")


# month = float(input("Enter the Month number: "))
# Year = float(input("Enter the Year: "))
    
# if((month==2) and ((year%4==0)  or ((year%100==0) and (year%400==0)))) :
#     print("Number of days is 29")

# elif(month==2) :
#     print("Number of days is 28")

# elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) :
#     print("Number of days is 31")

# else :
#     print("Number of days is 30")


# actual_cost = float(input(" Please Enter the Actual Product Price: "))
# sale_amount = float(input(" Please Enter the Sales Amount: "))
 
# if(actual_cost > sale_amount):
#     amount = actual_cost - sale_amount
#     print("Total Loss Amount = {0}".format(amount))
# elif(sale_amount > actual_cost):
#     amount = sale_amount - actual_cost
#     print("Total Profit = {0}".format(amount))
# else:
#     print("No Profit No Loss!!!")

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


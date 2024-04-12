#



# number = int(input("Enter a Number : "))

# if((number % 5 == 0) and (number % 11 == 0)):
#     print("Number is Divisible by 5 and 11".format(number))
# else:
#     print("Number is Not Divisible by 5 and 11".format(number)) 



# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))



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



# Problem 1 maximum between two numbers

# num1 = 10
# num2 = 20
# if num1 >= num2:
#    a = num1
# else:
#    a = num2
# print("Maximum is:", a)



# problem 2 maximum between three numbers

# num1 = 10
# num2 = 20
# num3 = 15

# if num1 >= num2 and num1 >= num3:
#    a = num1
# elif num2 >= num1 and num2 >= num3:
#    a = num2
# else:
#    a = num3
# print("Maximum is:",a)



# Problem 3 check whether a number is positive, negative or zero

# num = float(input("Enter a number: "))
# if num > 0:
#    print("Positive number")
# elif num == 0:
#    print("Zero")
# else:
#    print("Negative number")



# Problem 4 check whether a number is divisible by 5 and 11 or not

# num = int(input("Enter a number:"))
# if ((num % 5 == 0)and(num % 11 == 0)):
#    print("Number is divisible by 5 and 11")
# else:
#    print("Number is not divisible by 5 and 11")



# Problem 5 check whether a number is even or odd

# num = int(input("Enter a number:"))
# if num % 2 == 0:
#    print("Even")
# else:
#    print("Odd")



# Problem 6 check whether leap year or not

# num = int(input("Enter a year:"))
# if (num % 4 == 0):
#    print("is a Leap yerar")
# else:
#    print("is not a leap yerar")



# Problem 7 check whether a character is alphabet or not

# ch = input("Enter a character:")
# if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
#    print(ch,"is an alphabet")
# else:
#    print(ch,"is not an alphabet")



# Problem 8 check whether it is vowel or constant

# ch = input("Enter a character:")
# if ((ch == 'a') and (ch == 'e') and (ch == 'i') and (ch == 'o') and (ch == 'u') and
#     (ch == 'A') and (ch == 'E') and (ch == 'I') and (ch == 'I') and (ch == 'U')):
#    print(ch, "is an vowel")
# else:
#    print(ch, "Constant")
      
# ch = input("Enter a character:")
# if ch in ['a','A','e','E','i','I','o','O','u','U']:
#    print("is a vowel")
# else:
#    print("is not a vowel")



# Problem 9 check whether a character is alphabet, digit or special character

# ch = input("Enter a character:")
# if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
#    print(ch, "is alphabet")
# elif (ch >= '0' and ch <= '9'):
#    print(ch, "is digit")
# else:
#    print(ch, "is special character")



# Problem 10 check whether a character is Uppercase or Lowercase
# ch = input("Enter a character:")
# if ((ch >= 'A' and ch <= 'Z')):
#    print(ch, "is uppercase alphabet")
# elif ((ch >= 'a' and ch <= 'z')):
#    print(ch, "is lowercase alphabet")
# else:
#    print(ch, "is not an alphabet")
       


# problem 11 to enter week number and print day of week

# day = int(input("Enter a week number (1-7):"))
# if day == 1:
#    print('Monday')
# elif day == 2:
#    print('Tuesday')
# elif day == 3:
#    print('Wednersday')
# elif day == 4:
#    print('Thursday')
# elif day == 5:
#    print('Friday')
# elif day == 6:
#    print('Saturday')
# elif day == 7:
#    print('Sunday')
# else:
#    print('Invalid input ! Plese enter a number from 1 to 7.')



# Problem 12 find number of days in month

# month = int(input("Enter month number (1-12):"))
# if month == 1:
#    print("It contains 31 days")
# elif month == 2:
#    print("It contains 28 or 29 days")
# elif month == 3:
#    print("It contains 31 days")
# elif month == 4:
#    print("It contains 30 days")
# elif month == 5:
#    print("It contains 31 days")
# elif month == 6:
#    print("It contains 30 days")
# elif month == 7:
#    print("It contains 31 days")
# elif month == 8:
#    print("It contains 30 days")
# elif month == 9:
#    print("It contains 31 days")
# elif month == 10:
#    print("It contains 30 days")
# elif month == 11:
#    print("It contains 31 days")
# elif month == 12:
#    print("It contains 30 days")
# else:
#    print("Invlaid input ! enter a number from 1-12 ")



# Problem 13 to count total number of notes in given amount

# amount = int(input("Enter an amount:"))
# print("Press 1 for 2000rs note")
# print("Press 2 for 500rs note")
# print("Press 3 for 200rs note")
# print("Press 4 for 100rs note")
# print("Press 5 for 50rs note")
# print("Press 6 for 20rs note")
# print("Press 7 for 10rs note")
# print("Press 8 for 5rs coin")
# print("Press 9 for 2rs coin")
# print("Press 10 for 1rs coin")
# option = int(input("Enter your option:"))
# if option == 1:
#    result = amount/2000
#    print("No.Of 2000rs notes:", result)
# elif option == 2:
#    result = amount/500
#    print("No.Of 500rs notes:", result)
# elif option == 3:
#    result = amount/200
#    print("No.Of 200rs notes:", result)   
# elif option == 4:
#    result = amount/100
#    print("No.Of 100rs notes:", result) 
# elif option == 5:
#    result = amount/50
#    print("No.Of 50rs notes:", result)
# elif option == 6:
#    result = amount/20
#    print("No.Of 20rs notes:", result)
# elif option == 7:
#    result = amount/10
#    print("No.Of 10rs notes:", result)
# elif option == 8:
#    result = amount/5
#    print("No.Of 5rs coins:", result)
# elif option == 9:
#    result = amount/2
#    print("No.Of 2rs coins:", result) 
# elif option == 10:
#    result = amount/1
#    print("No.Of 1rs coins:", result)
# else:
#    print("Invalid value") 



# Problem 14 check whether triangle is valid or not if angles are given

# first_angle = int(input("Enter the first angle:"))      
# second_angle = int(input("Enter the second angle:"))      
# third_angle = int(input("Enter the third angle:"))
# sum = first_angle + second_angle + third_angle
# if (sum == 180 and first_angle > 0 and second_angle > 0 and third_angle > 0):
#    print("Triangle is valid")
# else:
#    print("Triangle is not valid")  



# Problem 15 check whether triangle is valid or not if angles are given

# first_side = int(input("Enter the first side:")) 
# second_side = int(input("Enter the second side:")) 
# third_side = int(input("Enter the third side:"))
# if((first_side + second_side) > third_side):
#    if((second_side + third_side) > first_side):
#       if((third_side + first_side) > second_side):
#          print("Triangle is valid")
#       else:
#          print("Triangle is not valid")
#    else:
#       print("Triangle is not valid")
# else:
#    print("Triangle is not valid")
   
# first_side = int(input("Enter the first side:")) 
# second_side = int(input("Enter the second side:")) 
# third_side = int(input("Enter the third side:"))
# if((first_side + second_side) > third_side):
#    print("Triangle is valid")
# elif((second_side + third_side) > first_side):
#    print("Triangle is valid")
# elif((third_side + first_side) > second_side):
#    print("Triangle is valid")
# else:
#    print("Triangle is not valid")



# Problem 16 check whether triangle is equilateral, scalene or isosceles

# first_side = int(input("Enter the first side:")) 
# second_side = int(input("Enter the second side:")) 
# third_side = int(input("Enter the third side:"))
# if((first_side == second_side) and (second_side == first_side)):
#    print("Equilateral triangle")
# elif((first_side == second_side) or (first_side == third_side) or (second_side == third_side)):
#    print("Isosceles triangle")
# else:
#    print("Scalene triangle")



# Problem 17 calculate profit or loss

# Cost_price = int(input("Enter a cost price:"))
# Selling_price = int(input("Enter a selling price:"))
# amt = 0
# if(Cost_price < Selling_price):
#    amt = Selling_price - Cost_price
#    print("Profit:", amt)
# elif(Cost_price > Selling_price):
#    amt = Cost_price - Selling_price
#    print("Loss:", amt)
# else:
#    print("No profit No loss")



# Problem 18 enter student marks and find percentage and grade

# Tam = int(input("Enter a tamil mark:"))
# Eng = int(input("Enter a english mark:"))
# Math = int(input("Enter a maths mark:"))
# Sci = int(input("Enter a science mark:"))
# Soc = int (input("Enter a social mark:"))
# per = ((Tam + Eng + Math + Sci + Soc)/ 5.0)
# print("Percentage =", per)
# if(per >= 90):
#    print("Grade A")
# elif(per >= 80):
#    print("Grade B")
# elif(per >= 70):
#    print("Grande C")
# elif(per >= 60):
#    print("Grade D")
# elif(per >= 40):
#    print("Grade E")
# else:
#    print("Grade F")



Problem 19
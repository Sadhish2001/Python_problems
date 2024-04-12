# W3 resource problems

# problem 1
# for i in range(1,11):
#     print(i, end=" ")



# problem 2
# sum = 0
# for i in range(1, 11):
#     sum = sum + i
#     print(i, end=" ")
# print("The sum is :",sum)



# problem 3
# sum = 0
# for i in range(1, 8):
#     sum = sum + i
#     print(i, end=" ")
# print("The sum of 7th term is : ",sum)



# problem 4
# Sum = 0
# print("Enter the Numbers\n")
# for i in range(1, 11):
#     num = int(input("Number %d = " %i))
#     Sum = Sum + num
#     avg = Sum / 10
# print("The Sum of 10 Numbers     =", Sum)
# print("The Average of 10 Numbers =", avg)



# problem 5
# number = float(input("Enter any numeric Value : "))
# cube = number * number * number
# print("The Cube of a Given Number {0}  = {1}".format(number, cube))

# num = int(input("Input number of terms: "))
# for i in range(1, num + 1):
#     cube = i ** 3
#     print("Number is :", i, "and cube of", i, "is", cube)



# problem 6
# num = int(input("Enter a table no:"))
# for i in range(1, 11):
#    print(num,'x', i,'=',num*i)



# # problem 7
# def display_multiplier_table(n):
#     for i in range(1, n+1):
#         print(f"Multiplication table for {i}:")    
#         for j in range(1, 11):
#             print(f"{i} x {j} = {i*j}")
# n = int(input("Table number starting from 1: "))
# display_multiplier_table(n)

# num = int(input("Input upto the table number starting from 1: "))
# print("")

# problem 8
# num = int(input("sum of natural numbers : "))
# sum = 0

# for i in range(1, num + 1):
#     if(not (i % 2) == 0):
#         sum += i

# print("\nSum of odd numbers from 1 to", num, "is :", sum)


# problem 9
# def display_triangle(rows):
    
#     for i in range(1, rows + 1):
#         print('*' * i)
        
# rows = int(input("Enter the number of rows for the triangle: "))
# display_triangle(rows)



# problem 10
# def display_triangle(rows):
    
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()

# rows = int(input("Enter the number of rows for the triangle: "))
# display_triangle(rows)


# problem 11
# def display_triangle(rows):
    
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             print(i, end=" ")
#         print()

# rows = int(input("Enter the number of rows for the triangle: "))
# display_triangle(rows)


# problem 12
# def print_increasing_number_triangle(n):
#     num = 1
    
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             print(num, end=" ")
#             num += 1
#         print()

# n = int(input("Enter the number of rows for the triangle: "))
# print_increasing_number_triangle(n)

# problem 13
# def print_number_pyramid(rows):
#     num = 1
    
#     for i in range(1, rows + 1):
#         print(" " * (rows - i), end="")
#         for j in range(1, i + 1):
#             print(num, end=" ")
#             num += 1
#         print()
        
# rows = int(input("Enter the number of rows for the pyramid: "))
# print_number_pyramid(rows)

# problem 14
# def print_number_pyramid(rows):
    
#     for i in range(1, rows + 1):
#         print(" " * (rows - i) + "*" * (2*i -1))   
#         print('*' * i)
          
# rows = int(input("Enter the number of rows for the triangle: "))
# print_number_pyramid(rows)


# def print_asterisk_pyramid(rows):
#     for i in range(1, rows + 1):
#         print(" " * (rows - i) + "*" * (2*i - 1))

# rows = int(input("Enter the number of rows for the pyramid: "))
# print_asterisk_pyramid(rows)


# problem 15
   
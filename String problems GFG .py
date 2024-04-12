# Check for Binary

# Example 2
# s = input("Enter string:")
# for i in s:
#     if i=="0" or i=="1":
#         print("1")
#         break
#     else:
#         print("0")

# Example 2    
# s = input("Enter string:")
# for i in s:
#     if i=="0" or i=="1":
#         print("1")
#         break
#     else:
#         print("0")
#         break



# Convert String to LowerCase

# s = input("Enter string:")
# o=""
# for i in s:
#     if "A" <= i <= "Z":
#         o += chr(ord(i)+32)
#     else:
#         o += i
# print(o)



# Remove Spaces

# s = input("Enter string:")
# for i in s:
#     if " " == i:
#         print(end="")
#     else:
#         print(i, end="")



# Reverse a String

# s = input("Enter string:")
# a = ""
# for i in s:
#     a = i+a
# print(a)



# Reversing the vowels

# s = ("practice")
# o = ""
# a = "AEIOUaeiou"
# for i in s:
#     if i in a:
#         o += i
# for i in s:
#     if i not in a:
#         o+=i
# print(o)



# Remove vowels from string

# s = input("Enter string:")
# o = ""
# vowels = "AEIOUaeiou"
# for i in s:
#     if i not in vowels:
#         o += i 
# print(o)



# Check String

# s = input("Enter string:")
# o = s == s[0] * len(s)
# print(o)



# Delete alternate characters

# s = input("Enter string:")
# o = ""
# for i in range(len(s)):
#     if i % 2==0:
#         o += s[i]
# print(o)



# count of camel case character

# s = input("Enter string:")
# n = 0
# for i in s:
#     if "A" <= i <= "Z":
#         n = n + 1
# print(n)



# count of string 

# s = "Sadhish"
# n=0
# for i in s:
#     n = n + 1
# print(n)



# Lowwer case to upper case 

# s = input("Enter string:")
# o=""
# for i in s:
#     if "a" <= i <= "z":
#         o += chr(ord(i)-32)
#     else:
#         o += i
# print(o)



# Count type of characters

# s = input("Enter string:")
# uppercase_char = 0
# lowercase_char = 0
# numeric_char = 0
# special_char = 0
# for i in s:
#     if 'A' <= i <= 'Z':
#         uppercase_char += 1
#     elif 'a' <= i <= 'z':
#         lowercase_char += 1
#     elif '0' <= i <= '9':
#         numeric_char += 1
#     else:
#         special_char += 1
# print(uppercase_char)
# print(lowercase_char)
# print(numeric_char)
# print(special_char)



# Remove characters from alphanumeric string

# s = input("Enter string:")
# o = ""
# for i in s:
#     if '0' <= i <= '9':
#         o += i
# print(o)



# Pattern of string

# Example 1
# s = input("Enter string:")
# for i in range(len(s),0,-1):
#     print(s[:i])

#Example 2
# s = input("Enter string:")
# for i in range(len(s)):
#     print(s[:len(s)-i])



# Split string

# s = input("Enter string:")
# s1 = ""
# s2 = ""
# s3 = ""
# for i in s:
#     if ('a'<= i <='z')or('A'<= i <='Z'):
#         s1 += i
#     elif '0'<= i <='9':
#         s2 += i
#     else:
#         s3 += i   
# print(s1)
# print(s2)
# print(s3)



# Triangle shrinking downwards

# s = input("Enter string:")
# for i in range(len(s)):
#     print('.' * i + s[i:])



# check prime no or not

# s = int(input("Enter string:"))

# if s > 1:
#     for i in range(2, s):
#         if (s % i) == 0:
#             print("Not a prime number")   
#             break
#     else:
#         print("Prime number")
# else:
#     print("Not a prime number")




# Maximum Occuring Character

# s = input("Enter string:")
# max_count = 0
# max_char = ""
# smallest_char = ""
# for i in s:
#     num = 0
#     for j in s:
#         if j == i:
#             num += 1
#     if num > max_count:
#         max_count = num
#         max_char = i
#         smallest_char = i
#     elif num == max_count and i < smallest_char:
#         smallest_char = i
# print(smallest_char)



# Uncommon characters

# a = "geeksforgeeks"
# b = "geeksquiz"
# o = ""
# c = a + b
# for i in c:
#     if i not in a or i not in b:
#         o += i
# print(o)



# Uncommon character in sorted order

# a = "geeksforgeeks"
# b = "geeksquiz"
# o = ""
# c = a + b
# for i in c:
#     if (i not in a) or (i not in b):
#         o += i
# sorted_o = ""
# for j in range(65, 123):
#     k = chr(j)
#     if k in o:
#         sorted_o += k
# print(sorted_o)



# Remove Consecutive Characters

# s = input("Enter string:")

# max_count = 0
# max_char = ""

# for i in s:
#     num = 0
#     for j in s:
#         if j == i:
#             num += 1
#         if num > max_count:
#             max_count = num
#             max_char = i
# print(max_char)

# s = input("Enter string:")

# max_count_a = 0
# max_count_b = 0

# for i in s:
#     num_a = 0
#     num_b = 0
#     for j in s:
#         if j == 'a':
#             num_a += 1
#         elif j == 'b':
#             num_b += 1
#     if num_a > max_count_a:
#         max_count_a = num_a
#     if num_b > max_count_b:
#         max_count_b = num_b

# max_char = ""
# if max_count_a >= max_count_b:
#     max_char += 'a'
# if max_count_b >= max_count_a:
#     max_char += 'b'

# print(max_char)



# S = input("Enter string:")
# o = ""
# for i in S:
#     if i in o:
#         print(i)
#         break
#     else:
#         o += i
# else:
#     print("-1")




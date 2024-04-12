# Problem 1 Value equal to index value

# num = int(input("Enter an element:"))
# s = [int(input("Enter list:")) for i in range(0,num)]
# o = 0
# for i in s:
#     o += 1
#     if i == o:
#         print(i)



# Problem 2 Print alternate elements of an array

# num = int(input("Enter an element:"))
# s = [int(input("Enter list:"))for i in range(num)]
# for i in range(num):
#     if i % 2 == 0:
#         print(s[i], end = " ")
        


# Problem 3 Count of smaller elements

# num = int(input("Enter an element:"))
# s = [int(input("Enter list:")) for i in range(0,num)]
# x = int(input("Enter an element:"))
# o = 0
# for i in s:
#     if i < x:
#         o += 1    
# print(o)


# Problem 4 Sum of Array

# num = int(input("Enter an element:"))
# s = [int(input("Enter list:"))for i in range(0,num)]
# o = 0
# for i in s:
#     o += i
# print(o)



# Problem 5 Print Elements of Array

# num = int(input("Enter an element:"))
# s = [int(input("Enter list:"))for i in range(0,num)]
# for i in s:
#     print(i, end = " ")



# Problem 6 Find Index

# num = int(input("Enter an element:"))
# s = [int(input("Enter list:")) for i in range(0,num)]
# x = int(input("Enter an key:"))
# a = -1
# b = -1
# for i in range(num):
#     if s[i] == x:
#         if a == -1:
#             a = i
#         b = i
# print("{", a, ",", b, "}")



# Problem 7 Swap kth elements

# num = int(input("Enter an element:"))
# x = int(input("Enter an element:"))
# s = [int(input("Enter list:")) for i in range(0,num)]
# s[x - 1], s[-x] = s[-x], s[x - 1]
# print(s)



# Problem 8 Display longest name

# Example 1
# num = int(input("Enter an element:"))
# s = [(input("Enter list:")) for i in range(0,num)]
# a = 0
# b = ""
# for i in s:
#     o = 0
#     for j in i:
#         o += 1
#     if o > a:
#         a = o
#         b = i
# print(b)

# Example 2
# num = int(input("Enter an element:"))
# s = [(input("Enter list:")) for i in range(0,num)]
# a = 0
# b = ""
# for i in s:
#     if len(i) > a:
#         a = len(i)
#         b = i
# print(b)



# Problem 9 Perfect Arrays

# num = int(input("Enter an element:"))
# s = [(input("Enter list:")) for i in range(0,num)]
# if s == s[::-1]:
#     print("PERFECT")
# else:
#     print("NOT PERFECT")



# Problem 10 Replace all 0's with 5

# num = int(input("Enter a number:"))
# a = 0
# b = 1
# while num > 0:
#     o = num % 10
#     if o == 0:
#         o = 5
#     a += o*b
#     num //= 10
#     b *= 10
# print(a)



# Problem 11 Average in a stream

# num = int(input("Enter an element:"))
# s = [int(input("Enter a list:"))for i in range(num)]
# o = 0
# for i in range(num):
#     o += s[i]
#     average = o / (i + 1)
#     print("%.2f" % average, end=" ")



# Problem 12 Sort the list

# num = int(input("enter an element:"))
# s = [int(input("Enter a list:"))for i in range(num)]
# s.sort()
# for i in s:
#     print(i, end= " ")

# num = int(input("enter an element:"))
# s = [int(input("Enter a list:"))for i in range(num)]
# while s:
#     a = min(s)
#     print(a, end=" ")
#     s.remove(a)
    
    

# Problem 13 At least two greater elemen/ts

# s = [1,2,3,4,5]
# s = [int(input("Enter a list:"))for i in range(num)]
# s.sort()
# for i in range(len(s)):
#     count = len(s) -i- 1
#     if count >= 2:
#         print(s[i], end=" ")



# l=[21,101,30501,450]
# summ=0
# mul=1
# def check(summ,mul):
#     l1=[]
#     l=[21,101,30501,450]
#     for i in range(0,len(l)):
#         if summ % l[i]==0 and mul % l[i]==0:
#             l1.append(0)
#         else:
#             l1.append(1)
#     return l1

# for i in range(0,len(l)):
#     while(l[i] > 0):
#         m = l[i] % 10
#         if m == 0:
#             mul = mul * 1
#         else:
#             summ = summ + m
#             mul = mul * m
#             l[i]=l[i]//10
#     print(check(summ,mul))


n = 4
arr = {1,4,3}
a = n * (n + 1) // 2
arr_sum = sum(arr)
missing_number = a - arr_sum
print(missing_number)
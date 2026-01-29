# Example:
# Input: "Hello world hello"
# Output:

# hello → 2
# world → 1


# a = "hello world hello"
 
# letter = ''
# b = []

# for i in a:
#     if i == " ":
#         b.append(letter)
#         letter = ""
#     else:
#         letter = letter + i
# b.append(letter)

# print(b)
# new = []
# count = 0
# for j in b:
#     for k in b:
#         if j == k:
#             count = count + 1
#     print(count )
#     break  





# def find(a):
#     count = 0
#     for i in a:
#         # if count <0:
#         #     return print(False)
#         #     break
#         if i == "(":
#             count = count +1
#         elif i == ")":
#             count = count - 1
#     if count == 0:
#         print(True)
#     else:
#         print(False)
# find("(((()))")


# def rev(n):
#     a = n[:2]
#     mid = ""
#     b = ""
#     print(len(n))
#     for i in range(len(n)-3,1,-1):
#         mid = mid + n[i]
#         print(mid)
#     for j in range(len(n)-2,len(n)):
#         b = b + n[j]
#         print(b)
#     print(a+mid+b)
# rev("fastapi")


# def count_word(a):
#     count = 0
#     b = a.split(" ")
#     for i in b:
#         for j in b:
#             if i ==  j:
#                 count = count + 1
#         break
#     print(count)
# count_word("hello world hello")

# def find (a):
#     count = 0
#     for i in a:
#         if count <0:
#             return print(False)
            
#         if i == '(':
#             count = count+1
#         elif i == ')':
#             count = count-1
            
#     if count == 0:
#         print(True)
#     else:
#         print(False)
        
# find("())(")
    

# Level 4 Problems for Monday:
# Given an array of Positive integers, count the number of prime numbers in it. Sample Input: {8, 14, 11, 23, 6}, Output: 2
# The output prints the stars in an inverted pyramid pattern based on the number of rows.
# Sample Input 1:
# 3
# Sample Output 1:
# * * * * *
#  * * *
#   *

# a = {8, 14, 11, 23, 6,7,13}
# count = 0
# for i in a:
#     if i ==1 :
#         count = count+1
#     elif i == 2:
#         count = count + 2
#     if i %3 !=0 and i% 5 !=0 and i%2 !=0:
#         count = count +1
# print(count)

x = [[1,2,3]
    ,[4,5,6]
    ,[7,8,9]]
    

for i in range(0,len(x)):
    
    if i == 0:
        for j in x[i]:
            print(j)
    elif i == len(x) -1:
        for k in x[i][::-1]:
            print(k)
        for m in range(1,len(x)-1):
            print(x[m][0])
           
    else:
        for i in range(1,len(x)-1):
            print(x[i][len(x[i])-1])
            
        
   
        
    

























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


















        
        
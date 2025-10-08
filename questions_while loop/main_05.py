# Find the sum of numbers from 1 to 100 using a while loop.

# a = 1
# b = 100
# sum = 0

# while a <=b:
#     sum = sum +a 
#     a = a+1
# print(sum)




#  Print the multiplication table of a number entered by the user (e.g., table of 5).


# n = int(input("enter the value of n"))
# a = 1
# b= 10
# while a <=b:
#     print(n*a)
#     a = a+1


#  Print numbers from 10 down to 1 using a while loop.

# n = 1
# a = 10

# while a >=n:
#     print(a)
#     a = a- 1




#  Keep asking the user to enter a number until they type the correct secret number.


n = int(input("enter the value of n :"))
a = 15
while n != a:
    print ("your answer is wrong ")
    n = int(input("enter the value of n :"))
    if n == a:
        print("your answer is correct :",a)
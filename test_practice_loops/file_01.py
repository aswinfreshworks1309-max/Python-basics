#  Print the multiplication table of a given number (say 5).

n = int(input("enter the value of n :"))
a = 1
b = 10

while a <=b:
    print(a*n)
    a = a+1
 
# Print the even numbers between 1 and 20.

a = 1
b = 20
while a <= b:
    if a % 2 == 0:
        print(a)
    a = a+1

# Print each character in a string "Python" using a for loop.

 

# right angle triangle

a = 5
b = 1
 
while a >= b:
    print ("*"*a)
    a = a-1


# Write a program to reverse a string using a loop.

a = "aswin"
for i in a[::-1]:
    print(i)
 

# Count how many vowels (a, e, i, o, u) are in a given string.

a =  "blastroise"
sum = 0
for i in a :
    sum = sum+1
print (sum)


# Print all numbers from 1 to 50 that are divisible by both 3 and 5.

a = 1
b = 50

while a<=b:
    if a %3 == 0 and a%5 == 0:
        print(a)
    a = a+1

# Write a program to check if a number is prime (using a loop).

n = int(input("enter the value of n :"))

if n>1:
    sum = True
    for i in range (2,n):
        if n%i == 0:
            sum = False
            break
    if sum:
        print("it is a prime number")
    else:
        print("it is not a prime number")
else:
    print("it is not a prime number")    

# Generate the first 10 Fibonacci numbers using a loop.

a = 0
b = 1
print(a,b, end= " ")
for i in range (8):
    num = a+b
    print(num, end= " ")
    a = b
    b = num

# Print a triangle pattern like this (using nested loops):

# *
# **
# ***
# ****
# *****

for i in range (1,5+1):
    print("*"*i)


# Print a multiplication table (1 to 10) in a grid format using loops.


 
for i in range(1,11):
    for j in range(1,11):
        print(i * j , end="\t")
    print()
 
 

 



# Find the factorial of a number using a loop.

n = int(input("enter the value of n :"))
a = 1
while a<=n:
    b = n*a
    fact = fact*b
    n = n-1
    print (fact)


# Write a program that asks the user for numbers until they type 0, then prints the sum of all entered numbers.

# Print all prime numbers between 1 and 100 using loops.

n = int(input("enter the value of n :"))
sum =  0


# Print all prime numbers between 1 and 100 using loops.

# Print prime numbers between 1 and 100

n = int(input("enter the value of x :"))
fact = 1
while 1<n:
    fact = fact*n
    n = n-1
print(fact)


n = int(input("entr the calue of x :"))
fact=1
for i in range (n,1,-1):
    fact = fact*i
print(fact)



 

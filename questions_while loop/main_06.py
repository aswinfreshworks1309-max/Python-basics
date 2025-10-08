# Find the sum of digits of a number (e.g., 123 → 1+2+3 = 6).

# num = int(input("Enter a number: "))
# total = 0

# while num > 0:
#     digit = num % 10       # get last digit
#     total += digit         # add to sum
#     num = num // 10        # remove last digit

# print("Sum of digits:", total)

n = int(input("enter the value of n :"))
sum = 0
while n >0:
    dig = n %10
    sum += dig
    n = n//10
    print("n value is :", n)
print(sum)


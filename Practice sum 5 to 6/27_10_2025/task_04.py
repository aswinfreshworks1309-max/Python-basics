# Write a Python program to find the sum of digits of a number (don’t convert to string).
#  Example:
#  Input → 987
#  Output → 24 (9 + 8 + 7)

n = 987
result = 0
while n >0:
    result = result + (n%10)
    n = n//10
print(result)
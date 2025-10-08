# a = int(input("Enter the value of a:"))
# b = int(input("Enter the value of b:"))
# c = int(input("Enter the value of c:"))

# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# elif c>a and c>b:
#     print(c)



a = int(input("Enter the amount"))
x = (a*10/100)
y = (a*5/100)
if a >=1000:
    print(a-x)
elif a>=500 and a< 1000:
    print(a-y)
elif a<500:
    print("Better luck next time  Deepika")
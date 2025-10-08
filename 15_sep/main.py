x = int(input("enter the value of x :"))
y = int(input("enter the value of y :"))

if x>0 and y>0:
    print("quadrant 1")
elif x<0 and y>0:
    print("quadrant 2")
elif x<0 and y<0:
    print("quadrant 3")
elif x>0 and y<0:
    print("quadrant 4")
else:
    print("point existence o,o")
    
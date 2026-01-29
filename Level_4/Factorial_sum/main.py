a = [2,3,4,5]
result = []
value = 1
for i in range(len(a)):
    while a[i]>0:
        value = value * a[i]
        a[i] = a[i]-1
    a[i] = value
    value =1
print(a)
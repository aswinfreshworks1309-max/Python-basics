a = [6,4,7,3,8,2,9,1]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j] < a[i]:
            a[j],a[i] = a[i],a[j]
print(a)
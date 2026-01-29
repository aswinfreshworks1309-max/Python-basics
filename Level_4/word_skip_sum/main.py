a = "programming"
b = "gramm"
f = 0
 
for i in range(len(a)):
    for j in range(len(a)):
        s = a[i:i+j]
        if s == b:
            f = i
for k in range(len(a)):
    if k >= f and k <= f+(len(b)-1):
        continue
    else:
        print(a[k])
        
 
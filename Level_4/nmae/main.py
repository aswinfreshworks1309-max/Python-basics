a = 'alice'
b = 'ice'
for i in range(len(a)):
    for j in range(i,len(a)):
        s = a[i:j+1] 
        if s == b:
            print(True)
            break
        else:
            print(False)
 
        
if b in a:
    print(True)
else:
    print(False)
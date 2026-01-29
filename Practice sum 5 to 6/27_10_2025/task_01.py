
def names(num):
    n = []
    for i in num:
        if i >0:
            n.append(i)
    print(n)
    
    a = len(num)-len(n)
    
    for i in range(1,a+1):
        n.append(0)
    print(n)
        
        
names([0, 1, 0, 3, 12])
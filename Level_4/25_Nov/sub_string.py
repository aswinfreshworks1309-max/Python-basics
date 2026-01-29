def find_substring(arr):
 

    count = 0
    for i in range(len(arr)):
        a = 0
        p = 1
        for j in range(i,len(arr)):
            p = p*arr[j]
            a = a+arr[j]
            if a == p:
                count = count +1
    return count
     
                        
print(find_substring([1,2,3]))




 
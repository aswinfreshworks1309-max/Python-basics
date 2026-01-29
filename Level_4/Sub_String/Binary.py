# 1. Longest Substring With Equal 0s and 1s

# Given a binary string, find the longest substring that contains an equal number of 0s and 1s.
# Return the substring length.

# Example:
# Input: "010110" → Output: 6
a = "01011010"
res = ''
count=0
plus = 0

for i in range(len(a)):
    count = 0
    plus = 0
    for j in range(i,len(a)):
        b = a[i:j+1]
       
        for k in b:
            if k == '0':
                count = count+1
            if k == '1':
                plus = plus +1
        if count == plus:
            if len(b)> len(res):
                res = b
     
 
print(len(res))
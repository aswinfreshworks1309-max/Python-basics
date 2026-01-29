a = [[1,2,3,4,5,6,7,8],[5,7,4,23,231,2323],[24,42,24,42,44,424,24,24]]
# sample output  [[1,2,3,4] ,[5,7,4] ,[24,42,24,42]]
b = []

for i in a:
    i = i[:len(i)//2]
    b.append(i)
print(b)







# for i in a:
#     i = i[:len(i)//2]
#     b.append(i)
# print(b)
 
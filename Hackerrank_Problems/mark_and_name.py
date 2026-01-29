arr = [['aswin',90],['alice',80]]
r = []
for i in arr:
    r.append(i[1])
 
s = max(r)
r.remove(s)
n = max(r)
print(n)

for j in arr:
    if j[1] == n:
        print(j[0])
 
#factorial problem

n = int(input("enter the value of n :"))
fact = 1

while n>1:
    fact = n *fact
    #   120=1*120
    n = n -1
  
print (fact)

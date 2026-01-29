a = input("Enter your input Here : ")

st=["chennai","bengalurr","delhi"]
sumer=[15,60,59]
monsoon=[79,90,54]
winter=[23,56,78]


def find_large(a):
    count = a[0]
    for i in range(len(a)):
        if a[i] > count :
            count = a[i]
    print(st[i])

if a == "sumer":
    find_large(sumer)
if a == "monsoon":
    find_large(monsoon)
if a == "winter":
    find_large(winter)
 


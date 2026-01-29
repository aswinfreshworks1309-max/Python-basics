def fact(a):
    if a == 0:
        return "invalid"
    elif a == 1:
        return 1
    elif a > 1:
        return a* fibo(a-1)
    
print(fact(5))
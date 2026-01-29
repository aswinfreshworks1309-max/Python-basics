def find_number(num):
    first_number = num[0]
    for i in num:
        if i >first_number:
            first_number = i
    num.remove(first_number)
   
    second_number = num[0]
    for i in num:
        if i >second_number:
            second_number = i
    print(second_number)
  
        
find_number([10, 40, 30, 20, 50])
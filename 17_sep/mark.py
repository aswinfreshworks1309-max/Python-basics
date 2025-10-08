mark = int(input("enter your mark :"))

print(mark)

match mark:
	case a if  mark <=100 and mark >= 80:
		print("A")
	case a if 79 >= mark >= 60:
		print("B")
	case _ if 59 >= mark >= 50:
		print("C")
	case _ if 49 >= mark >= 40:
		print("D")
	case _:
		print("Fail")	
    
    
    
 
    
    
    
    
 
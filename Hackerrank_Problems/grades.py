def gradingStudents(grades):
    
    for i in grades:
        
        if i < 38:
            print(i)
        else:
            s = ((i//5+1)*5)
            print(s)
          
            if (s - i) < 3:
                print(s)
            else:
                print(i)
                
            
                
gradingStudents([73,67,38,33])
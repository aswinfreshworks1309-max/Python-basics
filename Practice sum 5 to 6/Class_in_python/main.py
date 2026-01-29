class Section_b:
    def __init__(name,student_1,student_2,student_3):
        name.student_1 = student_1
        name.student_2 = student_2
        name.student_3 = student_3
        name.student_4 = "Alice"
    def expose_name(name):
       
        print(f"the name of the student_1 is : {name.student_1} \n the name of the student_2 is {name.student_2} \nnewly added student : {name.student_3}")
        
        
    def find_girl(name):
        print( "Newly added girl is :",name.student_4)
new = Section_b("Hanisha","Aswin","Irfana")

new.expose_name()

new.find_girl()
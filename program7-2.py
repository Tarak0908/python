class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
def print_student_info(student):
        print(f"name:{student.name}marks:{student.marks}")
s1=Student("tillu",92)
print_student_info(s1)




name:tillumarks:92

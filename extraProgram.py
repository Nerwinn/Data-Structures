# Ccollection of objects
class Student:
    def __init__(self, username, lastname, course, section):
        self.username = username
        self.lastname = lastname
        self.course = course
        self.section = section

    def introduction(self):
        print(f"Hi i am {self.username} {self.lastname} from {self.course} {self.section}")


registeredStudent = []

while True:
    print()
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    course = input("Enter your course: ")
    section = input("Enter your section: ")

    #ADDING THE USERS INPUT TO THE LIST
    addStudent = Student(fname, lname, course, section)
    registeredStudent.append(addStudent)

    #ASKING IF THE USERS WANT TO ADD MORE STUDENTS
    print()
    question = input("Do you want to add more? [Y/N]: ")
    if question == 'Y' or question == 'y':
        pass
    else:
        break

i=1
for student in registeredStudent:
    print()
    print("Student #", i)
    student.introduction()
    i+=1
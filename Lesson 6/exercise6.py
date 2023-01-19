# Let's create a simplified version of CUNYfirst

# INSTRUCTIONS
# Create a class called "Student" with the following properties: name, age, and major. Include a __init__ method that assigns these properties when an instance of the class is created.
# Create a method called "display_info" that prints the name, age, and major of the student.
# Create a class called "Course" with the following properties: name, instructor, and students (a list of Student objects). Include a __init__ method that assigns these properties when an instance of the class is created.
# Create a method called "add_student" that takes a Student object and adds it to the list of students in the course.
# Create a method called "remove_student" that takes a name and removes the student with that name from the list of students in the course.
# Create a method called "display_students" that prints the name and major of each student in the course, separated with a colon.
# Outside your classes, create a test() function that does the following:
#   Create 2 instances of your Student class called student1 and student2.
#   Call the display_info() method on both of your student objects
#   Create an instance of your Course class called course, and add student1 when you initialize the students property.
#   Add student2 to your course using the add_student() method
#   Remove student1 from the course using the remove_student() method
#   Call the display_students() method on your course object
# Run the test function.

# SOLUTION:

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.major)


class Course:
    def __init__(self, name, instructor, students=[]):
        self.name = name
        self.instructor = instructor
        self.students = students

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def display_students(self):
        for student in self.students:
            print(student.name + ": " + student.major)


def test():
    student1 = Student("Anthony Butta", 21, "Finance")
    student2 = Student("Marco Coluccio", 21, "Finance")

    student1.display_info()
    student2.display_info()

    course = Course("ACC 2101", "Harry Davis", [student1])

    course.add_student(student2)
    course.remove_student(student1)
    course.display_students()


test()

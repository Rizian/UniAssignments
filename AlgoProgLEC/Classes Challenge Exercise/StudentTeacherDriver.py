from StudentTeacherClasses import *

teacher1 = Teacher("Dave", "222 Grove Street")
print(teacher1)
teacher1.addCourse("Mathematics")
teacher1.addCourse("English")
teacher1.removeCourse("Mathematics")

teacher2 = Teacher("Ray", "789 Milky Way Avenue")
print(teacher2)
teacher2.addCourse("Programming")
teacher2.addCourse("Mathematics")
print(teacher2.addCourse("Mathematics"))


student1 = Student("John", "123 Rainbow Road")
print(student1)
student1.addCourseGrade("English", 80)
student1.addCourseGrade("Programming", 59)
student1.addCourseGrade("Mathematics", 77)
student1.printGrades()
print(student1.getAverageGrade())

student2 = Student("Jack", "100 Rainbow Road")
print(student2)
student2.addCourseGrade("English", 30)
student2.addCourseGrade("Programming", 70)
student2.addCourseGrade("Mathematics", 82)
student2.printGrades()
print(student2.getAverageGrade())
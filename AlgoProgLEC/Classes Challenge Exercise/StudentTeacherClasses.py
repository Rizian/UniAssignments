class Person:
    "This is the base class representing a person."

    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def getName(self) -> str:
        return self.__name
    def getAddress(self) -> str:
        return self.__address
    
    def setAddress(self, address):
        self.__address = address

    def __str__(self) -> str:
        return f"{self.getName()}({self.getAddress()})"

class Student(Person):
    "This is the class representing a student."

    def __init__(self, name, address, numCourses = 0):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.__courses = {}     # {"course": int(grade)}

    def addCourseGrade(self, course, grade):
        self.__courses[str(course)] = int(grade)

    def printGrades(self):
        for course in self.__courses:
            print(f"{course}: {self.__courses[course]}")
    
    def getAverageGrade(self) -> float:
        total_grade = 0
        for course in self.__courses:
            total_grade += self.__courses[course]
        average_grade = total_grade / len(self.__courses)
        return round(average_grade, 2)

    def __str__(self) -> str:
        return f"Student: {super().__str__()}"

class Teacher(Person):
    "This is the class representing a teacher."

    def __init__(self, name, address, numCourses = 0):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.__courses = []

    def addCourse(self, courseName):
        if str(courseName) in self.__courses:
            return False
        self.__courses.append(str(courseName))
        self.__numCourses += 1

    def removeCourse(self, courseName):
        if str(courseName) not in self.__courses:
            return False
        self.__courses.remove(str(courseName))
        self.__numCourses -= 1

    def __str__(self) -> str:
        return f"Teacher: {super().__str__()}"

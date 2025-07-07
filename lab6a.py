#!/usr/bin/env python3
# Author ID: tloo1

class Student:

    # Define name and number 
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Ensure number is string 
        self.courses = {}

    # Return student name and number
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    # Add grade and courses
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the GPA
    def displayGPA(self):
        if len(self.courses) == 0:
            return 'GPA of student ' + self.name + ' is 0.0'
        gpa = sum(self.courses.values())
        return 'GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses))

    # Return a list of courses that the student passed
    def displayCourses(self):
        passed_courses = []
        for course in self.courses:
         if self.courses[course] > 0.0:
            passed_courses.append(course)
        return passed_courses

if __name__ == '__main__':
    # Create first student object 
    student1 = Student('John', '013454900') 
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object 
    student2 = Student('Jessica', 123456) #Integer but converted to strings
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())

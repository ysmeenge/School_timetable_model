from enum import Enum

classes = ["1a", "1b"]  # enums


class Course(Enum):
    PE = 0
    ARTS = 1
    MATH = 2


# class Teacher:
#     def __init__(self, classes: [Subject]=[]):
#         self.classes = classes


class Teacher:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

    def what_does_teacher_teach(self):
        return self.subjects


timmy = Teacher("Timmy", ["Math", "English"])
jimmy = Teacher("jimmy", ["Math", "PE"])

timmy.subjects
timmy.what_does_teacher_teach()

teachers = [timmy, jimmy]
[teacher.subjects for teacher in teachers] == [["Math", "English"], ["Math", "PE"]]


class Classroom:
    pass


class Students:
    pass


# example Enum


class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)
print(type(Season.SPRING))
print(repr(Season.SPRING))
print(list(Season))

## testing

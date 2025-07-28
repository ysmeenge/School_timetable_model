classes = ['1a', '1b'] # enums

from enum import enum

class Subject(Enum):
    PE = 0
    ARTS = 1
    MATH = 2

class Teacher:
def __init__(self, classes: [Subject]=[]):
    self.classes = classes


class Classroom:
    pass

class Students:
    pass
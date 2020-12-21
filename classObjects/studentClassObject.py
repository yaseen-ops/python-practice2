class Student:

    def __init__(self, name, age, major, is_on_probation):
        self.name = name
        self.age = age
        self.major = major
        self.is_on_probation = is_on_probation

    def is_on_age_mark(self):
        if self.age <= 29:
           return True
        else:
            return False
class Mark:
    def __init__(self, mark):
        self.mark = mark
from classObjects.studentClassObject import Student
from classObjects.studentClassObject import Mark

student1 = Student("Jim", 29, "Driver", False)  # student1 is the object name
student2 = Student("David", 30, "Business", True)

print(student1.is_on_age_mark())
print(student2.is_on_age_mark())

student3 = Mark(73)
print(student3.mark)
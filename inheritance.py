class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
        
    def average(self):
        return sum(self.marks)/len(self.marks)
    
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name,school)
        self.salary = salary
    @property # convert method into property
    def weekly_salary(self):
        return self.salary * 37.5

rolf = WorkingStudent("Rolf", "MIT", 15.15)
rolf.marks.append(55)
rolf.marks.append(45)
rolf.marks.append(75)
print(rolf.average())
print(rolf.weekly_salary)
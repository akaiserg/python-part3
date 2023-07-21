class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades
    def average(self):
        return sum(self.grades) / len(self.grades)
    
student_one =  Student("Peter", [70, 88, 90, 45])

print(student_one.name)
print(student_one.__class__)
print(student_one.average())
#what Python does in the background
print(Student.average(student_one))



class Garage:
    def __init__(self):
        self.cars = []
    def __len__(self):
        return len(self.cars)
    def __getitem__(self, i):
        return self.cars[i]
    def __repr__(self):
        return f'<Garage {self.cars}>'
    def __srt__(self):
        return f'<Garage with {len(self)}>'
        
ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(ford[0]) # Garage.__getitem__(ford, 0)

print(ford)
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
        
    def average(self):
        return sum(self.marks)/len(self.marks)
    
rolf = Student('Rolf', 'MIT')
rolf.marks.append(23)
rolf.marks.append(53)
rolf.marks.append(63)

#print(rolf.average('hello'))

class Food:
    @classmethod
    def hi(cls):
        print(cls.__name__)
        
my_object = Food()
my_object.hi()

class Bar:
    @staticmethod
    def hi():
        print("Hello!")
    
my_bar = Bar()
my_bar.hi()
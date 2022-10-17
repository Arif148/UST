class Person:           # Parent Class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print("Hello Person")
        

class Student(Person):  # Child Class
    def __init__(self,name,age,gender,studentid,fees):
        Person.__init__(self,name,age,gender)
        self.studentid = studentid
        self.fees = fees

    def greet(self):
        print("Hello Student")

stud_obj = Student('Anu',23,'Female',12397, 15000)
stud_obj.greet()    # method defined in subclass/child class will be triggered 

person1 = Person('Arif',25,'Male')
person1.greet()    # method defined in superclass/parent class will be triggered

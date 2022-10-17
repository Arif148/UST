class Person:       # Parent Class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PersonInfo(self):
        print('Name : {}'.format(self.name))
        print('Age : {}'.format(self.age))
        print('Gender : {}'.format(self.gender))

# Child class
class student(Person):
    def __init__(self, name, age, gender, studentid, fees):
        # Result of inheritance
        Person.__init__(self,name,age,gender)
        self.studentid = studentid
        self.fees = fees

    def StudentInfo(self):
        print('Student ID : {}'.format(self.studentid))
        print('Fees : {}'.format(self.fees))

# Child Class
class teacher(Person):     
    def __init__(self, name, age, gender, empid, salary):
        person.__init__(self, name, age, gender)
        self.empid = empid
        self.salary = salary

    def TeacherInfo(self):
        print('Employee ID : {}'.format(self.empid))
        print('Salary : {}'.format(self.salary))

stud_obj = student('Shibin',25,'Male',12345,10000)
print('Student Details :')
print('-----------------')
stud_obj.PersonInfo()       # PersonInfo() method present in Parent Class & it will be accessible
stud_obj.StudentInfo()
    


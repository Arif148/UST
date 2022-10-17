# Super() builtin function that allows us to access methods of base class.

class person:       # Parent Class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PersonInfo(self):
        print('Name : {}'.format(self.name))
        print('Age : {}'.format(self.age))
        print('Gender : {}'.format(self.gender))

class student(person):    # Child Class
    def __init__(self, name, age, gender,studentid,fees):
        super().__init__(name,age,gender)
        self.studentid = studentid
        self.fees = fees

    def StudentInfo(self):
        super().PersonInfo()
        print('Sudent ID : {}'.format(self.studentid))
        print('Fees : {}'.format(self.fees))

stu_obj = student('Pooja', 25, 'Female', 12398, 10000)
stu_obj.StudentInfo()

class person:       # Parent Class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PersonInfo(self):
        print('Name : {}'.format(self.name))
        print('Age : {}'.format(self.age))
        print('Gender : {}'.format(self.gender))

class employee(person):     # Child Class
    def __init__(self, name, age, gender, empid, salary):
        person.__init__(self, name, age, gender)
        self.empid = empid
        self.salary = salary

    def employeeInfo(self):
        print('Emp Id : {}'.format(self.empid))
        print('Salary : {}'.format(self.salary))

class fulltime(employee):       # Grand Child Class
    def __init__(self, name, age, gender, empid, salary, WorkExperience):
        employee.__init__(self, name, age, gender, empid, salary)
        self.WorkExperience = WorkExperience

    def FullTimeInfo(self):     
        print('Work Experience : {}'.format(self.WorkExperience))

class contractual(employee):    # Grand Child Class
    def __init__(self, name, age, gender, empid, salary, ContractExpiry):
        employee.__init__(self, name, age, gender, empid, salary)
        self.ContractExpiry = ContractExpiry

    def ContractInfo(self):
        print('Contract Expiry : {}'.format(self.ContractExpiry))

print('Contractual Employee Details:')
print('*****************************')
contr_obj = contractual('Pooja', 25, 'Female', 12398, 70000, '31-12-2022')
contr_obj.PersonInfo()
contr_obj.employeeInfo()
contr_obj.ContractInfo()

print('Fulltime Employee Details:')
print('*****************************')
full_obj = fulltime('Suresh', 31, 'Male', 12399, 50000, 5)
full_obj.PersonInfo()
full_obj.employeeInfo()
full_obj.FullTimeInfo()

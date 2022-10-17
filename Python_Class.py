# Create an Employee Class
class Employee:
    def __init__(self, name, empid):   # __init__() function is used to assign values.
        self.name = name
        self.empid = empid

    def greet(self):
        print('Thanks for joining XYZ Company {} !!'.format(self.name))

# Create an Employee Object
emp1 = Employee("Arjun",78923)      # Create an employee object.

print('Name : ', emp1.name)
print('Employee ID : ', emp1.empid)
emp1.greet()

# Create another Employee Object
emp2 = Employee('Anu', 78924)

print('Name : ', emp2.name)
print('Employee ID : ', emp2.empid)
emp2.greet()

emp2.country = 'India'   # Instance variable can be created manually.
print (emp2.country)

# Modify Object Properties
emp1.name = 'Aryan'
print(emp1.name)

# Delete Object Properties
del(emp1.empid)
# This will give an Error - Attribute Error
#emp1.empid

# Delete an Object
del(emp1)
# This will give an Error - Name Error
emp3 = Employee('Arif', 78925)
emp3.name




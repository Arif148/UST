# Python Classes - Example 2
import datetime
class Person:
    def __init__(self, name, surname, birthdate, address, phone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.phone = phone
        self.email = email
        
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

person = Person('Arif','Ahmed',datetime.date(1994, 12, 24),    # year, month, day
                'No. 12 Random Street, Golflinks Villa, Hyderdabad',
                '9988776655', 'arif.ahmed@example.com')

print(person.name)
print(person.email)
print(person.age())

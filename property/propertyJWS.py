from propertyMain import Person
person = Person("진", "우석", 24)
print(person.age)

person.age = 40
print(person.age)

person.age = -1        #ValueError  
print(person.age)
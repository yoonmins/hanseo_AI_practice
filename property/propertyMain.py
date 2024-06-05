class Person:
    def __init__(self, firtst_name, last_name, age):
        self.first_name = firtst_name
        self.last_name = last_name
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        if age<0:
                raise ValueError("Invalid age")
        self._age =age
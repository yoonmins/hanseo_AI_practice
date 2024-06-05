class Person:
    def __init__(self, firtst_name, last_name, age):
        self.first_name = firtst_name
        self.last_name = last_name
        self._age = age

    def get_age(self):
        return self._age
    
    def set_age(self,age):
        if age<0:
                raise ValueError("Inalid age")
        self._age =age
    
    age = property(get_age, set_age)
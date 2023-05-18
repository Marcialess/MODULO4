class Empleado:
    sueldo = 0


    def __init__(self, _name):
        self.name = _name

person = Empleado("Marcial Abad")
print(person.name)

class EmpleadoProtected:
    sueldo = 0
    def __init__(self, _name):
        self.__name = _name

    @property 
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self, _name):
        self.__name = _name

person2 = EmpleadoProtected("Maria")

print(person2.name)        



